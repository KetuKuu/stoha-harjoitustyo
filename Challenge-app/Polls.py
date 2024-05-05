
from flask import render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from flask import render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from db import db

#Polls
def get_polls():

    sql = "SELECT id, topic, created_at FROM polls ORDER BY id DESC"
    result = db.session.execute(text(sql))
    polls = result.fetchall()
    return polls

def create_polls():

    topic = request.form["topic"]
    sql = "INSERT INTO polls (topic, created_at) VALUES (:topic, NOW()) RETURNING id"
    result = db.session.execute(text(sql), {"topic":topic})
    poll_id = result.fetchone()[0]
    choices = request.form.getlist("choice")
    for choice in choices:
        if choice != "":
            sql = "INSERT INTO choices (poll_id, choice) VALUES (:poll_id, :choice)"
            db.session.execute(text(sql), {"poll_id":poll_id, "choice":choice})
    db.session.commit()

    return {"poll_id": poll_id, "topic": topic, "choices": choices}


def choose_poll(id):
        
    sql = "SELECT topic FROM polls WHERE id=:id"
    result = db.session.execute(text(sql), {"id":id})
    topic = result.fetchone()[0]
    sql = "SELECT id, choice FROM choices WHERE poll_id=:id"
    result = db.session.execute(text(sql), {"id":id})
    choices = result.fetchall()

    return topic, choices

def poll_answer(poll_id, choice_id ):

        sql = "INSERT INTO answers (choice_id, sent_at) VALUES (:choice_id, NOW())"
        db.session.execute(text(sql), {"choice_id":choice_id})
        db.session.commit()

def get_poll_results(id):
    sql = "SELECT topic FROM polls WHERE id=:id"
    result = db.session.execute(text(sql), {"id": id})
    topic = result.fetchone()[0]
    sql = "SELECT c.choice, COUNT(a.id) FROM choices c LEFT JOIN answers a " \
          "ON c.id=a.choice_id WHERE c.poll_id=:poll_id GROUP BY c.id"
    result = db.session.execute(text(sql), {"poll_id": id})
    choices = result.fetchall()
    return topic, choices
     



