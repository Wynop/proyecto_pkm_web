from flask import Flask, render_template, request, session, redirect, url_for
import json, random

app = Flask(__name__, template_folder="templates")
app.secret_key = "algo"

with open("data/pokemons-eeveelutions.json", "r", encoding="utf-8") as archivo:
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
def pkmList():
    if "name" not in session:
        return redirect(url_for("index"))
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

            return render_template(
                "battle.html", pkmAtq=pkmSel, pkmDef=pkmRand, pkmAtqMoves=pkmAtqMoves
            )
        elif action == "filter":
            filterName = request.form["pokemon"].strip().lower()
            filterType = request.form["type"]
            output = []

            for pkm in data:
                if filterName in pkm["name"].lower() and (
                    not filterType or filterType in pkm["types"]
                ):
                    output.append(pkm)

            return render_template(
                "pkmList.html", data=output, abv=abv, types=types, filter=[filterName,filterType]
            )

    return render_template(
        "pkmList.html",
        data=data,
        abv=abv,
        types=types,
    )


@app.route("/pkm/<int:id>")
def pkmData(id):

    pokemon = {}

    for pkm in data:
        if pkm["id"] == id:
            pokemon = pkm
            break

    return render_template("pkmData.html", pkm=pokemon)


if __name__ == "__main__":
    app.run(port=8080, debug=True)
