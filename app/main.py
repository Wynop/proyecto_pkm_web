from flask import Flask
from flask_session import Session
from routes.pokemon import pokemon
from routes.auth import auth
from routes.battle import battleBp
from config.config import Config
from pathlib import Path

from config.constants import PokemonStat, PokemonType

app = Flask(__name__, template_folder="templates")

app.register_blueprint(auth)
app.register_blueprint(pokemon)
app.register_blueprint(battleBp)

app.config.from_object(Config)
app.jinja_env.globals["PokemonStat"] = PokemonStat
app.jinja_env.globals["PokemonType"] = PokemonType

Session(app)

ruta = Path(app.root_path) / "templates" / "index.html"

if __name__ == "__main__":
    app.run(port=8080, debug=True)
