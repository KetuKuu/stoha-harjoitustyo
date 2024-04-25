from flask import Flask
from flask import render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from os import getenv
from werkzeug.security import check_password_hash, generate_password_hash
from db import db





def mark_done(user_id, region, card_id):
    try:
        # Tarkista, onko merkintä jo olemassa
        existing = db.session.execute(
            text("SELECT id FROM completions WHERE user_id=:user_id AND card_id=:card_id AND region=:region"),
            {"user_id": user_id, "card_id": card_id, "region": region}
        ).fetchone()

        if existing:
            # Poista olemassa oleva merkintä
            db.session.execute(
                text("DELETE FROM completions WHERE id=:id"),
                {"id": existing[0]}
            )
        else:
            # Lisää uusi merkintä
            db.session.execute(
                text("INSERT INTO completions (user_id, card_id, region, completion_date) VALUES (:user_id, :card_id, :region, NOW())"),
                {"user_id": user_id, "card_id": card_id, "region": region}
            )
        
        db.session.commit()
        return True
    except Exception as e:
        print(f"Error while marking done: {e}")
        return False
    
def get_user_completions(user_id):
    sql = "SELECT card_id FROM completions WHERE user_id=:user_id"
    result = db.session.execute(text(sql), {"user_id": user_id})
    return set(result.scalars().all())


def create_card(title, description, image_url, region):
        sql = "INSERT INTO cards (title, description, image_url, region) VALUES (:title, :description, :image_url, :region)"
        db.session.execute(text(sql), {"title": title, "description": description, "image_url": image_url, "region": region})
        db.session.commit()

def get_all_cards():
    sql = "SELECT id, title, description, image_url, region, created_at FROM cards ORDER BY created_at DESC"
    result = db.session.execute(text(sql))
    cards = result.fetchall()
    return cards

def get_card_by_id(card_id):
    sql = "SELECT id, title, description, image_url, region, created_at FROM cards WHERE id = :card_id"
    result = db.session.execute(text(sql), {"card_id": card_id})
    card = result.fetchone()
    return card