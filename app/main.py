from flask import Flask
from flask_session import Session
from routes.pokemon_routes import pokemon_bp
from routes.auth_routes import auth_bp
from routes.battle_routes import battle_bp
from config.config import Config
from pathlib import Path

from config.constants import PokemonStat, PokemonType

app = Flask(__name__, template_folder="templates")

app.register_blueprint(auth_bp)
app.register_blueprint(pokemon_bp)
app.register_blueprint(battle_bp)

app.config.from_object(Config)
app.jinja_env.globals["PokemonStat"] = PokemonStat
app.jinja_env.globals["PokemonType"] = PokemonType

Session(app)

ruta = Path(app.root_path) / "templates" / "index.html"

if __name__ == "__main__":
    app.run(port=8080, debug=True)
