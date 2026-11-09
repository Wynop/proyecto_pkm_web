from flask import Blueprint, request, render_template, redirect, url_for, session
from functools import wraps

from services.logsService import LogsService
from forms.authForm import LoginForm

auth = Blueprint("auth", __name__)


def login_requerido(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if "name" not in session:
            return redirect(url_for("auth.index"))
        return func(*args, **kwargs)

    return wrapper


@auth.route("/", methods=["GET", "POST"])
def index():
    form = LoginForm()
    if request.method == "POST" and form.validate_on_submit():
        name = form.trainer.data
        res = LogsService.logIn(name)

        if res[0]:
            return redirect(url_for("pokemon.pkmList"))
        else:
            return render_template("index.html", error=res[1], form=form)

    if "name" not in session:
        return render_template("index.html", disabled=True, form=form)

    return render_template("index.html", form=form)


@auth.route("/logout")
def logout():
    LogsService.logOut()
    return redirect(url_for("auth.index"))