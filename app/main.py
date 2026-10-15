from flask import Flask, render_template, request, session, redirect, url_for
import json

app = Flask(__name__)
app.secret_key = 'algo'

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

@app.route("/saveName", methods=["POST"])
def saveName():
    name = request.form["name"]

    if len(name) < 3 or len(name) > 15:
        return "El nombre debe tener entre 3 y 15 caracteres", 400

    session["name"] = name

    return redirect(url_for("pkmList"))
@app.route("/savePkm", methods=["POST"])
def savePkm():
    pkm = request.form["pkm"]

    session["pkm"] = pkm

    return redirect(url_for("battle"))

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))

@app.route("/pkm-list")
def pkmList():
    if "name" not in session:
        return redirect(url_for("index"))
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
