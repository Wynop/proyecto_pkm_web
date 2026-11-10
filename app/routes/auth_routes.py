from flask import Blueprint, request, render_template, redirect, url_for, session
from functools import wraps

from forms.auth_form import LoginForm

auth_bp = Blueprint("auth_routes", __name__)


def login_requerido(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if "name" not in session:
            return redirect(url_for("auth_routes.index"))
        return func(*args, **kwargs)

    return wrapper


@auth_bp.route("/", methods=["GET", "POST"])
def index():
    form = LoginForm()
    if request.method == "POST" and form.validate_on_submit():
        name = form.trainer.data.strip()

        if len(name) < 3 or len(name) > 15:
            return render_template("index.html", error="The name must be between 3 and 15 characters long.", form=form)
        session["name"] = name
        return redirect(url_for("pokemon_routes.pkm_list"))

    if "name" not in session:
        return render_template("index.html", disabled=True, form=form)

    return render_template("index.html", form=form)


@auth_bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("auth_routes.index"))