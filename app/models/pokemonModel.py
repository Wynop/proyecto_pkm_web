from dataclasses import dataclass
from models.moveModel import Move
import json

@dataclass
class Pokemon:
    id: int
    name: str
    height: int
    weight: int
    types: list[str]
    stats: dict[str, int]
    sprites: list[str]
    moves: list[Move]

    @classmethod
    def from_dict(cls, pkm: dict) -> "Pokemon":
        return cls(
            id=pkm["id"],
            name=pkm["name"],
            height=pkm["height"],
            weight=pkm["weight"],
            types=pkm["types"],
            stats={s["name"]: s["value"] for s in pkm["stats"]},
            sprites=list(pkm["sprites"].values()),
            moves=[Move(**m) for m in pkm["moves"]],
        )

def cargarPkm(ruta: str) -> list[Pokemon]:
    with open(ruta, encoding="utf-8") as f:
        return [Pokemon.from_dict(p) for p in json.load(f)]

    