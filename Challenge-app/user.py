from flask import Flask
from flask import render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from os import getenv
from werkzeug.security import check_password_hash, generate_password_hash
from db import db



def get_user(username,password):

    sql = "SELECT id, password FROM users WHERE username=:username"
    result = db.session.execute(text(sql), {"username":username})
    user = result.fetchone()
    if not user:
        hash_value = generate_password_hash(password)
        # Insert new user to the database
        sql = "INSERT INTO users (username, password) VALUES (:username, :password)"
        db.session.execute(text(sql), {"username":username, "password":hash_value})
        db.session.commit()
        
        #return redirect("/loging")
        return "new_user_created" 
    
    else:
        hash_value = user.password
        if check_password_hash(hash_value, password):    
            session["username"] = username
            print("session[\"username\"]: ", session["username"])
            return "login_successful"
        else:
            error_message = "Incorrect username or password"
            #return render_template("loging.html", error_message=error_message)
            return "login_failed"



def logout():
    del session["username"]
    #return redirect("/loging")
    return redirect("/Frontpage")
