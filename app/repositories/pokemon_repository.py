from models.pokemon_model import Pokemon
import json
from pathlib import Path

class PokemonRepository:
    RUTA_POR_DEFECTO = Path(__file__).resolve().parents[2] / "data" / "pokemons-eeveelutions.json"

    def __init__(self, ruta: Path = RUTA_POR_DEFECTO):
        self._ruta = ruta
        self._pokemons = None

    def obtener_pkm(self) -> list[Pokemon]:
        if self._pokemons is None:
            self._pokemons = self._cargar_datos()
        return self._pokemons

    def _cargar_datos(self) -> list[Pokemon]:
        with open(self._ruta, encoding="utf-8") as f:
            return [Pokemon.from_dict(p) for p in json.load(f)]