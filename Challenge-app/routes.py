from app import app
import user
import Polls
import my_info
import Card
import utils
import card_update
import tasks
from flask import render_template, request, redirect, session, url_for
import os


@app.route("/")
def index1():
    # Ohjaa käyttäjä Frontpage-näkymään
    return redirect(url_for("home")) 

@app.route("/Frontpage")
def home():
    cards = Card.get_all_cards()
    user_id = session.get("user_id")

    if user_id:
        completions = tasks.get_user_completions(user_id)
    else:
        completions = set()

    return render_template("Frontpage.html", cards=cards, completions=completions)


#user

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
            error_message = "Väärä käyttäjätunnus tai salasana"
            return render_template("loging.html", error_message=error_message) 

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


# task

@app.route("/myinfo")
def myinfo():
    user_id = session.get("user_id")
    if user_id is None:
        return redirect("/login")

    completion_count = my_info.get_user_completions(user_id)
    return render_template("myinfo.html", completion_count=completion_count)


#mark card 

@app.route("/mark-done", methods=["POST"])
def mark_done():
    if 'username' not in session:
        return redirect(url_for("login"))
    
    user_id = session.get("user_id")
    region = request.form.get("region")
    card_id = request.form.get("card_id")
    #done = Card.mark_done(user_id, region, card_id)   
    done = tasks.mark_done_get(user_id, region, card_id)  

    if done:
        return redirect("/Frontpage")
    else:
        return "Error", 400 


#create card

@app.route("/addcard", methods=["GET"])
def show_add_card_form():
    return render_template("addcard.html")   


@app.route("/created", methods=["POST"])
def create_card():

    if request.method == "POST":
        title = request.form['title']
        description = request.form['description']
        region = request.form['region']
        file = request.files['image']
      

    if file and utils.allowed_file(file.filename):
        filename = utils.secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        Card.create_card(title, description, filepath, region, session['user_id'])  # Kutsu card.py moduulin funktiota
        return redirect("/Frontpage")
    return "Error", 400


#update card

@app.route("/card_detail/<int:card_id>", methods=["GET"])
def card_detail(card_id):
    card = Card.get_card_by_id(card_id)
    images = card_update.get_image_by_id(card_id)
    if card:
        return render_template("challenge_detail.html", card = card, images = images) 
    else:
        return "Card not found", 404 

@app.route("/update_image/<int:card_id>", methods=["POST"])
def update_image(card_id):

    if request.method == "POST":
        image = request.files['image']
        description = request.form['description']
        title = request.form.get('title')

    if image and utils.allowed_file(image.filename):
        filename = utils.secure_filename(image.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        image.save(filepath)
        
        #tallennus
        user_id = session.get("user_id")
        card_update.update_image(card_id, user_id, filename, title, description) # Kutsu card_detail.py moduulin funktiota
        return redirect(f"/card_detail/{card_id}")
    return "Error", 400

