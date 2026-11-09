from flask import Blueprint, session, render_template

from routes.auth import login_requerido

battleBp = Blueprint("battle", __name__)

@battleBp.route("/battle")
@login_requerido
def battle():
    battleData = session.get("battle")

    return render_template(
        "battle.html",
        pkmAtq=battleData[0],
        pkmDef=battleData[1],
        pkmAtqMoves=battleData[0].moves
    )