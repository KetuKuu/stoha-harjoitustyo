from flask import Flask
from flask import render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from os import getenv
from werkzeug.security import check_password_hash, generate_password_hash
from db import db





def mark_done(user_id, region):
    try:
        # Tarkista, onko merkintä jo olemassa
        existing = db.session.execute(
            text("SELECT id FROM completions WHERE user_id=:user_id AND region=:region"),
            {"user_id": user_id, "region": region}
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
                text("INSERT INTO completions (user_id, region, completion_date) VALUES (:user_id, :region, NOW())"),
                {"user_id": user_id, "region": region}
            )
        
        db.session.commit()
        return True
    except Exception as e:
        print(f"Error while marking done: {e}")
        return False
