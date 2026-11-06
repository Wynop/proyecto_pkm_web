from dataclasses import dataclass

@dataclass
class Move:
    name: str
    url: str
    accuracy: int | None
    power: int | None
    type: str