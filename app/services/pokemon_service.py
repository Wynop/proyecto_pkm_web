class PokemonService:

    def __init__(self, repo):
            self.repo = repo

    def get_all_pkm(self):
        return self.repo.obtener_pkm()
    
    def get_pkm_id(self, id):
        for pkm in self.repo.obtener_pkm():
            if pkm.id == id:
                return pkm
                
        return None
    

    def get_pkm_filtered(self, name: None, type: None):
        output = []
        for pkm in self.repo.obtener_pkm():
            if (
                (not name or name in pkm.name.lower())
                and (not type or type in pkm.types)
            ):
                output.append(pkm)
        return output