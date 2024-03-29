class Pokemon:
    def __init__(self, name, starter, id, ids_ataques):
        self.name = name
        self.starter = starter
        self.psalud = 100
        self.pdefensa = 100
        self.ids_ataques = ids_ataques
        self.attacks = []
        self.id = id
        self.win = 0