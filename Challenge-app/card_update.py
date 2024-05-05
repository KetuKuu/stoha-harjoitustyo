from flask import Flask
from flask import render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from os import getenv
from werkzeug.security import check_password_hash, generate_password_hash
from db import db


#card_update

def update_image(card_id, user_id, filename, title, description):
    sql = "INSERT INTO card_media (card_id, user_id, image_filename, title, description) VALUES (:card_id, :user_id, :image_filename, :title, :description)"
    db.session.execute(text(sql), {"card_id": card_id,"user_id": user_id,"image_filename": filename,"title": title,"description": description})
    db.session.commit()

def get_image_by_id(card_id):
    sql = "SELECT image_filename, title, description FROM card_media WHERE card_id = :card_id"
    result = db.session.execute(text(sql), {"card_id": card_id})
    image = result.fetchall()
    return image



