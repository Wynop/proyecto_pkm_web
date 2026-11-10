from flask import Blueprint, request, render_template, redirect, url_for

from config.constants import PokemonType
from forms.battle_from import BattleForm
from forms.filter_form import PokemonFilterForm
from config.deps import BATTLE_SERVICE, POKEMON_SERVICE
from routes.auth_routes import login_requerido

pokemon_bp = Blueprint("pokemon_routes", __name__)


@pokemon_bp.route("/pkm-list", methods=["GET", "POST"])
@login_requerido
def pkm_list():
    battle_form = BattleForm(prefix="battle-")
    filter_form = PokemonFilterForm(prefix="filter-")

    filter_form.type.choices = [("", "All types")] + [
        (pokemon_type.value, pokemon_type.value.capitalize())
        for pokemon_type in PokemonType
    ]

    name = request.args.get("name", "").strip().lower()
    pkm_type = request.args.get("type", "")

    if request.method == "POST":
        if battle_form.submit.data and battle_form.validate():
            battleGen = BATTLE_SERVICE.battle_random(
                battle_form.pokemon.data.lower()
            )

            if battleGen[0]:
                return redirect(url_for("battle_routes.battle"))

            errorBattle = battleGen[1]

        elif filter_form.submit.data and filter_form.validate():
            filterName = filter_form.pokemon.data.lower() if filter_form.pokemon.data else ""
            filterType = filter_form.type.data

            params = {}

            if filterName:
                params["name"] = filterName

            if filterType:
                params["type"] = filterType

            return redirect(url_for("pokemon_routes.pkm_list", **params))

        else:
            errorBattle = None

        return render_template(
            "pkmList.html",
            data=POKEMON_SERVICE.get_all_pkm(),
            battle_form=battle_form,
            filter_form=filter_form,
            errorBattle=errorBattle,
            filter=(name, pkm_type)
        )

    if name or pkm_type:
        data = POKEMON_SERVICE.get_pkm_filtered(name, pkm_type)
    else:
        data = POKEMON_SERVICE.get_all_pkm()

    filter_form.pokemon.data = name
    filter_form.type.data = pkm_type

    return render_template(
        "pkmList.html",
        data=data,
        battle_form=battle_form,
        filter_form=filter_form,
        filter=(name, pkm_type)
    )


@pokemon_bp.route("/pkm/<int:id>")
@login_requerido
def pkm_data(id):
    return render_template("pkmData.html", pkm=POKEMON_SERVICE.get_pkm_id(id))
