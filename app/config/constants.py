from enum import StrEnum


class PokemonType(StrEnum):
    NORMAL = "normal"
    FIRE = "fire"
    WATER = "water"
    ELECTRIC = "electric"
    GRASS = "grass"
    ICE = "ice"
    FIGHTING = "fighting"
    POISON = "poison"
    GROUND = "ground"
    FLYING = "flying"
    PSYCHIC = "psychic"
    BUG = "bug"
    ROCK = "rock"
    GHOST = "ghost"
    DRAGON = "dragon"
    DARK = "dark"
    STEEL = "steel"
    FAIRY = "fairy"


class PokemonStat(StrEnum):
    HP = "PS"
    ATTACK = "ATQ"
    DEFENSE = "DEF"
    SPECIAL_ATTACK = "AT.E."
    SPECIAL_DEFENSE = "DEF.E."
    SPEED = "VEL"