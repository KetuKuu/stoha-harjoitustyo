from app import app
import user
import Polls
import my_info
import Card
from flask import render_template, request, redirect, session, url_for


@app.route("/")
def index1():
    # Ohjaa käyttäjä Frontpage-näkymään
    return redirect(url_for("home")) 

""" @app.route("/")
def index():
    sisalto =["Australia""/page1", "Afrikka""/page2", "Asia" ]
    return render_template("index.html",message="Tervetuloa!", items=sisalto) """

@app.route("/Frontpage")
def home():
    return render_template("Frontpage.html")

#User


@app.route("/loging", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("loging.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if user.login(username, password):
            return redirect("/Frontpage")
        else:
            #return render_template("error.html", message="Väärä tunnus tai salasana")
            error_message = "Väärä käyttäjätunnus tai salasana"
            return render_template("loging.html", error_message=error_message)  # Kirjautuminen epäonnistui, näytä virheviesti"""


def user_id():
    return session.get("user_id", 0)

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]
        password1 = request.form["password1"]
        password2 = request.form["password2"]
        if password1 != password2:
            return render_template("error.html", message="Salasanat eroavat")
        if user.register(username, password1):
            return redirect("/Frontpage")
        else:
            return render_template("error.html", message="Rekisteröinti ei onnistunut")



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


# Order

""" @app.route("/order")
def order():

    return render_template("order.html")

@app.route("/result", methods=["POST"])
def result():
    pizza = request.form["pizza"]
    extras = request.form.getlist("extra")
    message = request.form["message"]
    return render_template("result.html", pizza=pizza,
                                          extras=extras,
                                          message=message)"""

# Task

@app.route("/myinfo")
def myinfo():
    user_id = session.get("user_id")
    print(f"Debug: User ID from session - {user_id}")
    if user_id is None:
        return redirect("/login")

    completion_count = my_info.get_user_completions(user_id)
    print(f"Debug: Completion count - {completion_count}")
    return render_template("myinfo.html", completion_count=completion_count)

#Card

@app.route("/europe1")
def europe():
    return render_template("europe1.html")


@app.route("/mark-done", methods=["POST"])
def mark_done():
    if 'username' not in session:
        return redirect(url_for("login"))
    
    user_id = session.get("user_id")
    region = request.form.get("region")
    done = Card.mark_done(user_id, region)
    

    if done:
        return redirect("/Frontpage")
    else:
        return "Error", 400
