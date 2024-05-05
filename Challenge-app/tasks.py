
from flask import render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from flask import render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from db import db

#tallentaa tietokantaan
def mark_done(user_id, region):
    try:
        sql = "INSERT INTO completions (user_id, region, completion_date) VALUES (:user_id, :region, NOW())"
        db.session.execute(sql, {"user_id": user_id, "region": region})
        db.session.commit()
        return True
    except Exception as e:
        print(f"Error while marking done: {e}")
        return False
    
def mark_done_get(user_id, region, card_id):
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