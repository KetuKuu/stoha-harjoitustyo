from flask import Flask, session, request, render_template, redirect
from flask import render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from os import getenv
from werkzeug.security import check_password_hash, generate_password_hash
from db import db
from datetime import datetime
import secrets


def login (username, password):
    sql = "SELECT id, password FROM users WHERE username=:username"
    result_user =db.session.execute (text(sql), {"username":username})
    user = result_user.fetchone()

    if not user:
        return False
    else:
        if check_password_hash(user.password, password):
            session["username"] = username 
            session["user_id"] = user.id
            session['csrf_token'] = secrets.token_hex(16) 
            return True
        else:
            return False

def register (username, password):
    # tarkistus ennen tallentamista
    if len(username) < 5 or len (username) > 20:
        return False
    
    if len(password) < 5:
        return False

    # Jos käyttäjätunnus on jo olemassa
    
    sql = "SELECT id, password FROM users WHERE username=:username"
    result = db.session.execute(text(sql), {"username":username})
    user = result.fetchone()
    if user:
        return False

    hash_value = generate_password_hash(password)
    try:
        sql = "INSERT INTO users (username, password) VALUES (:username, :password)"
        db.session.execute(text(sql), {"username":username, "password":hash_value})
        db.session.commit()
       
    except:
        return False
    return login(username, password)

def logout():
    del session["username"]
    #return redirect("/loging")
    return redirect("/Frontpage")


