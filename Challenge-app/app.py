from flask import Flask
from os import getenv,makedirs
from werkzeug.security import check_password_hash, generate_password_hash



app = Flask(__name__)
app.debug = True


# Määrittele tiedostojen tallennuspolku ja varmista, että kansio on olemassa
app.config['UPLOAD_FOLDER'] = 'static/uploads'
makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

import routes

