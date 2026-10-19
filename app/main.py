from flask import Flask, render_template, request, session, redirect, url_for
import json, random

app = Flask(__name__, template_folder='templates')
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
    if "name" not in session:
        return render_template("index.html", disabled=True)
    return render_template("index.html")

@app.route("/saveName", methods=["POST"])
def saveName():
    name = request.form["name"]

    if len(name) < 3 or len(name) > 15:
        return "El nombre debe tener entre 3 y 15 caracteres", 400

    session["name"] = name

    return redirect(url_for("pkmList"))

@app.route("/battle", methods=["POST"])
def battle():
    pkm = request.form["pokemon"].strip().lower()
    
    if not pkm:
        return render_template(
            "pkmList.html",
            data=data,
            abv=abv,
            error = "You must enter a Pokémon name."
        )
        
    pokemon = None
    
    for item in data:
        if item["name"].lower() == pkm:
            pokemon = item
            break

    if pokemon is None:
        return render_template(
            "pkmList.html",
            data=data,
            abv=abv,
            error="That Pokémon does not exist."
        )
    
    pkmRand = None
        
    while True:
        pkmRand = random.choice(data)
    
        if pkmRand["name"] != pokemon["name"]:
            break
            
    pkmAtqMoves = random.sample(pokemon['moves'], 4)

    return render_template("battle.html", pkmAtq=pokemon, pkmDef=pkmRand, pkmAtqMoves=pkmAtqMoves)

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))

@app.route("/pkm-list")
def pkmList():
    if "name" not in session:
        return redirect(url_for("index"))
    return render_template("pkmList.html", data=data, abv=abv)

@app.route("/filter")
def filter():
    return redirect(url_for("pkmList"))

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
