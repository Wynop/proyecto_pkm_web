from flask import Blueprint, session, render_template

from routes.auth_routes import login_requerido

battle_bp = Blueprint("battle_routes", __name__)

@battle_bp.route("/battle")
@login_requerido
def battle():
    battle_data = session.get("battle")

    return render_template(
        "battle.html",
        pkmAtq=battle_data[0],
        pkmDef=battle_data[1],
        pkmAtqMoves=battle_data[0].moves
    )