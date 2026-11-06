from flask import Flask, render_template, request, session, redirect, url_for
from flask_session import Session
from functools import wraps
import json, random
from pathlib import Path
from models.pokemonModel import Pokemon, cargarPkm

app = Flask(__name__, template_folder="templates")

app.config["SESSION_TYPE"] = "filesystem"   
app.config["SESSION_PERMANENT"] = False     
app.config["SESSION_FILE_DIR"] = "./.flask_session"  
app.secret_key = "clave_super_secreta"

Session(app)


ruta = Path(__file__).parent.parent / "data" / "pokemons-eeveelutions.json"

with open(ruta, "r", encoding="utf-8") as archivo:
    data = json.load(archivo)

abv = {
    "hp": "PS",
    "attack": "ATQ",
    "defense": "DEF",
    "special-attack": "AT.E.",
    "special-defense": "DEF.E.",
    "speed": "VEL",
}
types = [
    "normal",
    "fire",
    "water",
    "electric",
    "grass",
    "ice",
    "fighting",
    "poison",
    "ground",
    "flying",
    "psychic",
    "bug",
    "rock",
    "ghost",
    "dragon",
    "dark",
    "steel",
    "fairy",
]


pokemonCarga = cargarPkm(ruta)

print(pokemonCarga[1])

def login_requerido(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if "name" not in session:
            return redirect(url_for("index"))
        return func(*args, **kwargs)

    return wrapper


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["trainer"].strip()
        if len(name) < 3 or len(name) > 15:
            return render_template(
                "index.html", error="The name must be between 3 and 15 characters long."
            )
        session["name"] = name
        return redirect(url_for("pkmList"))

    if "name" not in session:
        return render_template("index.html", disabled=True)

    return render_template("index.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))


@app.route("/pkm-list", methods=["GET", "POST"])
@login_requerido
def pkmList():
    name = request.args.get("name", "").strip().lower()
    pkmType = request.args.get("type", "")

    if request.method == "POST":
        action = request.form.get("action")
        if action == "battle":
            pkm = request.form["pokemon"].strip().lower()

            if not pkm:
                return render_template(
                    "pkmList.html",
                    data=data,
                    abv=abv,
                    types=types,
                    errorBattle="You must enter a Pokémon name.",
                )
            pkmSel = None
            for item in data:
                if item["name"].lower() == pkm:
                    pkmSel = item
                    break
            if pkmSel is None:
                return render_template(
                    "pkmList.html",
                    data=data,
                    abv=abv,
                    types=types,
                    errorBattle="That Pokémon does not exist.",
                )

            pkmRand = None

            while True:
                pkmRand = random.choice(data)

                if pkmRand["name"] != pkmSel["name"]:
                    break

            pkmAtqMoves = random.sample(pkmSel["moves"], 4)

            session["battle"] = [pkmSel, pkmRand, pkmAtqMoves]

            return redirect(url_for("battle"))
        elif action == "filter":
            filterName = request.form["pokemon"].strip().lower()
            filterType = request.form["type"]

            params = {}

            if filterName:
                params["name"] = filterName

            if filterType:
                params["type"] = filterType

            return redirect(url_for("pkmList", **params))

    if name or type:
        output = []
        for pkm in data:
            if (
                (not name or name in pkm["name"].lower())
                and (not pkmType or pkmType in pkm["types"])
            ):
                output.append(pkm)

        return render_template(
            "pkmList.html",
            data=output,
            abv=abv,
            types=types,
            filter=[name, pkmType],
        )

    return render_template(
        "pkmList.html",
        data=data,
        abv=abv,
        types=types,
    )


@app.route("/pkm/<int:id>")
@login_requerido
def pkmData(id):

    pokemon = None

    for pkm in data:
        if pkm["id"] == id:
            pokemon = pkm
            break

    return render_template("pkmData.html", pkm=pokemon)


@app.route("/battle")
@login_requerido
def battle():
    battle = session.get("battle")
    return render_template(
        "battle.html", pkmAtq=battle[0], pkmDef=battle[1], pkmAtqMoves=battle[2]
    )


if __name__ == "__main__":
    app.run(port=8080, debug=True)
