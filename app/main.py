from flask import Flask, render_template
import json

app = Flask(__name__)

with open("data/pokemons-eeveelutions.json", "r", encoding="utf-8") as archivo:
    data = json.load(archivo)

abv = {
    "hp": "PS",
    "attack": "ATQ",
    "defense": "DEF",
    "special-attack": "AT.E.",
    "special-defense": "DEF.E.",
    "speed": "VEL"
}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/pkm-list")
def pkmList():
    return render_template("pkmList.html", data=data, abv=abv)


@app.route("/pkm/<int:id>")
def pkmData(id, abv=abv):

    pokemon = {}

    for pkm in data:
        if pkm["id"] == id:
            pokemon = pkm
            break

    return render_template("pkmData.html", pkm=pokemon)


if __name__ == "__main__":
    app.run(port=8080, debug=True)
