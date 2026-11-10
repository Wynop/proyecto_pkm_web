from dataclasses import dataclass
from models.move_model import Move

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
    def from_dict(self, pkm: dict) -> "Pokemon":
        return self(
            id=pkm["id"],
            name=pkm["name"],
            height=pkm["height"],
            weight=pkm["weight"],
            types=pkm["types"],
            stats={s["name"]: s["value"] for s in pkm["stats"]},
            sprites=list(pkm["sprites"].values()),
            moves=[Move(**m) for m in pkm["moves"]],
        )



    