from flask import Flask, url_for, request, render_template, redirect
import json
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

answer_params = {"title": "Анкета", "surname": "Watny", "name": "Mark", "education": "выше среднего", "profession": "штурман марсохода", "sex": "male", "motivation": "Всегда мечтал застрять на Марсе!", "ready": "True"}
astronauts = ["Ридли Скотт", "Энди Уир", "Марк Уотни", "Венката Капур", "Тедди Сандерс", "Шон Бин"]


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


@app.route("/list_prof/<list>")
def list_prof(list):
    jobs = ["инженер исследователь", "пилот", "сторитель", "экзобиолог", "врач", "инженер по терраформированию",
            "климатолог", "специалист по радиационной защите", "астрогеолог", "гляциолог", "инженер жизнеобеспечения",
            "метеоролог", "оператор марсохода", "киберинженер", "штурман", "пилот дронов"]
    return render_template("list_prof.html", type=list, jobs=jobs)


@app.route("/image_mars")
def mars_img():
    with open("templates/mars_img.html", encoding="utf8") as f:
        return f.read()


@app.route("/promotion_image")
def promotion_image():
    with open("templates/promotion_image.html", encoding="utf8") as f:
        return f.read()


@app.route("/astronaut_selection", methods=["POST", "GET"])
def astronaut_selection():
    if request.method == "GET":
        with open("templates/astronaut_selection.html", encoding="utf8") as f:
            return f.read()
    elif request.method == "POST":
        f = request.files
        return "Ваша заявка успешно оставлена"


@app.route("/load_photo", methods=["POST", "GET"])
def load_photo():
    if request.method == "GET":
        with open("static/images/loaded_photo", "w") as f:
            f.write("")
        with open("templates/load_photo.html", encoding="utf8") as f:
            return f.read()
    elif request.method == "POST":
        request.files["file"].save("static/images/loaded_photo")
        return open("templates/load_photo.html", encoding="utf8").read()


@app.route("/carousel")
def carousel():
    with open("templates/carousel.html", encoding="utf8") as f:
        return f.read()


@app.route("/choice/<planet_name>")
def choice(planet_name):
    return render_template("choice.html", planet_name=planet_name)


@app.route("/results/<nickname>/<int:level>/<float:rating>")
def results(nickname, level, rating):
    return render_template("results.html", nickname=nickname, level=level, rating=rating)


@app.route("/answer")
@app.route("/auto_answer")
def answer():
    return render_template("auto_answer.html", **answer_params)


@app.route("/distribution")
def distribution():
    return render_template("distribution.html", title="Размещение по каютам", astronauts=astronauts)


class LoginForm(FlaskForm):
    astronaut_id = StringField("id астронавта", validators=[DataRequired()])
    astronaut_password = PasswordField("Пароль астронавта", validators=[DataRequired()])
    captain_id = StringField("id капитана", validators=[DataRequired()])
    captain_password = PasswordField("Пароль капитана", validators=[DataRequired()])
    submit = SubmitField("Доступ")


@app.route("/login", methods=["POST", "GET"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect("/success")
    return render_template("login.html", title="Аварийный доступ", form=form)


if __name__ == "__main__":
    app.run(port=8000, host="127.0.0.1")