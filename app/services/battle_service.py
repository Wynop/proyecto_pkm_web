import random

from flask import session

class BattleService:

    def __init__(self, pkm_service):
        self.pkm_service = pkm_service


    def battle_random(self, pkm):
        
        if not pkm:
            return [False, "You must enter a Pokémon name."]
        
        data = self.pkm_service.get_all_pkm()
        battle_data = []
        
        for item in data:
            if item.name.lower() == pkm:
                battle_data.append(item)
                break
        
        if len(battle_data) == 0:
            return [False, "That Pokémon does not exist."]
        
        battle_data[0].moves = random.sample(battle_data[0].moves, 4)
    
        while True:
            pkm_rand = random.choice(data)
        
            if pkm_rand.name != battle_data[0].name:
                battle_data.append(pkm_rand)
                break
        
        session["battle"] = battle_data
        
        return [True, battle_data]
    