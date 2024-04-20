from app import app
import user
import Polls
from flask import render_template, request, redirect, session,url_for


@app.route("/")
def index1():
    # Ohjaa käyttäjä Frontpage-näkymään
    return redirect(url_for("home")) 

@app.route("/")
def index():
    sisalto =["Australia""/page1", "Afrikka""/page2", "Asia" ]
    return render_template("index.html",message="Tervetuloa!", items=sisalto)

@app.route("/Frontpage")
def home():
    return render_template("Frontpage.html")

#User

@app.route("/loging")
def loging():
    return render_template("loging.html")

@app.route("/login",methods=["POST"])
def login():

    username = request.form["username"]
    password = request.form["password"]
    login_result = user.get_user(username, password)
    
    if login_result == "new_user_created":
        return redirect("/loging")  # Uusi käyttäjä luotiin, ohjaa kirjautumissivulle
    elif login_result == "login_successful":
        return redirect("/Frontpage")  # Kirjautuminen onnistui, ohjaa etusivulle
    else:
        error_message = "Väärä käyttäjätunnus tai salasana"
        return render_template("loging.html", error_message=error_message)  # Kirjautuminen epäonnistui, näytä virheviesti

@app.route("/logout")
def logout():
    user.logout()
    return redirect("/Frontpage")

#polls

@app.route("/polls")
def pollsindex():
    polls= Polls.get_polls()
    return render_template("pollsindex.html", polls=polls)

@app.route("/pollsnew")
def pollsnew():
    return render_template("pollsnew.html")

@app.route("/create", methods=["POST"])
def create():
    created_poll=Polls.create_polls()
    return redirect("/polls")

@app.route("/poll/<int:id>")
def poll(id):
    topic, choices = Polls.choose_poll(id)
    return render_template("pollschoose.html", id=id, topic=topic, choices=choices)

@app.route("/answer", methods=["POST"])
def answer():
    poll_id = request.form["id"]
    choice_id = request.form["answer"]
    Polls.poll_answer(poll_id, choice_id)
    return redirect("/pollresults/" + str(poll_id))

@app.route("/pollresults/<int:id>")
def resultKysely(id):
    
    topic, choices = Polls.get_poll_results(id)
    return render_template("pollresults.html", topic=topic, choices=choices)

