from flask import Flask, url_for, request, render_template, redirect
import json
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route("/<title>")
@app.route("/index/<title>")
def index(title):
    return render_template("base.html", title=title)


@app.route("/training/<prof>")
def training(prof):
    if "инженер" in prof.lower() or "строитель" in prof.lower():
        t = "Инженерные симуляторы"
        src = "starship_scheme_eng_sim"
    else:
        t = "Научные тренажеры"
        src = "starship_scheme_sci_tr"
    return render_template("training.html", title="Тренировки", type=t, src=src)


if __name__ == "__main__":
    app.run(port=8000, host="127.0.0.1")