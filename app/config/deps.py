from repositories.pokemonRepository import PokemonRepository
from services.pokemonService import PokemonService
from services.logsService import LogsService
from services.battleService import BattleService

POKEMON_REPOSITORY = PokemonRepository()
POKEMON_SERVICE = PokemonService(POKEMON_REPOSITORY)
LOGS_SERVICE = LogsService(POKEMON_SERVICE)
BATTLE_SERVICE = BattleService(POKEMON_SERVICE)