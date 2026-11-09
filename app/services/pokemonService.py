from repositories.pokemonRepository import PokemonRepository

class PokemonService:
    
    @staticmethod
    def getAllPkm():
        return PokemonRepository.obtenerPkm()
    
    @staticmethod
    def getPkmById(id):
        for pkm in PokemonRepository.obtenerPkm():
            if pkm.id == id:
                return pkm
                
        return None
    
    @staticmethod
    def getPkmFiltered(name: None, type: None):
        output = []
        for pkm in PokemonRepository.obtenerPkm():
            if (
                (not name or name in pkm.name.lower())
                and (not type or type in pkm.types)
            ):
                output.append(pkm)
        return output