from models.pokemonModel import Pokemon
from pathlib import Path
import json

class PokemonRepository:
    rutaPkm = Path(__file__).resolve().parents[2] / "data" / "pokemons-eeveelutions.json"
    
    _pokemons = None

    @classmethod
    def obtenerPkm(self):
        if self._pokemons is None:
            self._pokemons= self._cargarPkm()
        return self._pokemons
    
    @staticmethod
    def _cargarPkm(ruta: str = rutaPkm):
        with open(ruta, encoding="utf-8") as f:
            return [Pokemon.from_dict(p) for p in json.load(f)]