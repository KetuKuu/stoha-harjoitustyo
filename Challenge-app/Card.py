from flask import Flask
from flask import render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from os import getenv
from db import db


#create_card

def create_card(title, description, image_url, region, user_id):
    sql = "INSERT INTO cards (title, description, image_url, region, user_id) VALUES (:title, :description, :image_url, :region, :user_id)"
    db.session.execute(text(sql), {"title": title, "description": description, "image_url": image_url, "region": region, 'user_id': user_id})
    db.session.commit()

def get_all_cards():
    sql = "SELECT id, title, description, image_url, region, created_at FROM cards ORDER BY created_at DESC"
    result = db.session.execute(text(sql))
    cards = result.fetchall()
    return cards

def get_card_by_id(card_id):
    sql = "SELECT id, title, description, image_url, region, created_at, user_id FROM cards WHERE id = :card_id"
    result = db.session.execute(text(sql), {"card_id": card_id})
    card = result.fetchone()
    print("Debug card info:", card)
    return card

def remove_card(card_id):
    #riippuvuudet completitions
    sql = "DELETE FROM completions WHERE card_id = :card_id"
    db.session.execute(text(sql), {"card_id": card_id})
    db.session.commit()
    #poisto cards
    sql = "DELETE FROM cards WHERE id = :card_id"
    db.session.execute(text(sql), {"card_id": card_id})
    db.session.commit()




