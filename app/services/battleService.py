import random

from flask import session

from services.pokemonService import PokemonService


class BattleService:
    
    @staticmethod
    def battleRandom(pkm):
        
        if not pkm:
            return [False, "You must enter a Pokémon name."]
        
        data = PokemonService.getAllPkm()
        battleData = []
        
        for item in data:
            if item.name.lower() == pkm:
                battleData.append(item)
                break
        
        if len(battleData) == 0:
            return [False, "That Pokémon does not exist."]
        
        battleData[0].moves = random.sample(battleData[0].moves, 4)
    
        while True:
            pkmRand = random.choice(data)
        
            if pkmRand.name != battleData[0].name:
                battleData.append(pkmRand)
                break
        
        session["battle"] = battleData
        
        return [True, battleData]
    