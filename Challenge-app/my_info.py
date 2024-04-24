
from flask import render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from flask import render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from db import db




def get_user_completions(user_id):
    sql = text("SELECT region, COUNT(*) as count FROM completions WHERE user_id=:user_id GROUP BY region")
    result_done = db.session.execute(sql, {"user_id": user_id})
    completion_count = result_done.fetchall()
    return {row.region: row.count for row in completion_count}
    #return {row['region']: row['count'] for row in completion_count}