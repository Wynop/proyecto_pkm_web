from flask import Blueprint, request, render_template, redirect, url_for

from config.constants import PokemonType
from forms.battleFrom import BattleForm
from forms.filterForm import PokemonFilterForm
from services.pokemonService import PokemonService
from services.battleService import battleService
from routes.auth import login_requerido

pokemon = Blueprint("pokemon", __name__)


@pokemon.route("/pkm-list", methods=["GET", "POST"])
@login_requerido
def pkmList():
    battleForm = BattleForm(prefix="battle-")
    filterForm = PokemonFilterForm(prefix="filter-")

    filterForm.type.choices = [("", "All types")] + [
        (pokemon_type.value, pokemon_type.value.capitalize())
        for pokemon_type in PokemonType
    ]

    name = request.args.get("name", "").strip().lower()
    pkmType = request.args.get("type", "")

    if request.method == "POST":
        if battleForm.submit.data and battleForm.validate():
            battleGen = battleService.battleRandom(
                battleForm.pokemon.data.lower()
            )

            if battleGen[0]:
                return redirect(url_for("battle.battle"))

            errorBattle = battleGen[1]

        elif filterForm.submit.data and filterForm.validate():
            filterName = filterForm.pokemon.data.lower() if filterForm.pokemon.data else ""
            filterType = filterForm.type.data

            params = {}

            if filterName:
                params["name"] = filterName

            if filterType:
                params["type"] = filterType

            return redirect(url_for("pokemon.pkmList", **params))

        else:
            errorBattle = None

        return render_template(
            "pkmList.html",
            data=PokemonService.getAllPkm(),
            battleForm=battleForm,
            filterForm=filterForm,
            errorBattle=errorBattle,
            filter=(name, pkmType)
        )

    if name or pkmType:
        data = PokemonService.getPkmFiltered(name, pkmType)
    else:
        data = PokemonService.getAllPkm()

    filterForm.pokemon.data = name
    filterForm.type.data = pkmType

    return render_template(
        "pkmList.html",
        data=data,
        battleForm=battleForm,
        filterForm=filterForm,
        filter=(name, pkmType)
    )


@pokemon.route("/pkm/<int:id>")
@login_requerido
def pkmData(id):
    return render_template("pkmData.html", pkm=PokemonService.getPkmById(id))
