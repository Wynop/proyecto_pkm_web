from repositories.pokemon_repository import PokemonRepository
from services.pokemon_service import PokemonService
from services.battle_service import BattleService

POKEMON_REPOSITORY = PokemonRepository()
POKEMON_SERVICE = PokemonService(POKEMON_REPOSITORY)
BATTLE_SERVICE = BattleService(POKEMON_SERVICE)