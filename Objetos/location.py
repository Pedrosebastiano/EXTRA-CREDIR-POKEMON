class Location:
    def __init__(self, name, id, ids_pokemones):
        self.name = name
        self.id = id
        self.ids_pokemones = ids_pokemones
        self.passed = False
        self.creatures = []

class Pueblo(Location):
    def __init__(self, name, id, ids_pokemones, lider_name):
        super().__init__(name, id, ids_pokemones)
        self.lider_name = lider_name
    
class Ruta(Location):
    def __init__(self, name, id, ids_pokemones):
        super().__init__(name, id, ids_pokemones)

class Liga(Location):
    def __init__(self, name,id, ids_pokemones, lider_name):
        super().__init__(name, id, ids_pokemones)
        self.lider_name = lider_name
