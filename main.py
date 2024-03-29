#IMPORTACION DE MODULOS
from Modulos.data_management import get_data, new_profile, select_starter
from Modulos.battle_pokemon import move_location, battle


class Game: 
    def __init__(self):
        self.player = None
        self.human_company = None
        self.company_starter = None
        self.locations = []
        self.starters = [] 
        self.attacks = []
        self.creatures = []

    def start_game(self):
        """Funcion principal que permite cargar la batalla, los datos e iniciar el juego
        No retorna, permite crear la instancia game"""
        get_data(self)
        print("-------------------------------------------------------------\n")
        print("                 🧙🪄 POKEMON TRIP 🪄🧙")
        print("\n-------------------------------------------------------------\n")
        self.player, self.human_company = new_profile(self)
        self.player.starter, self.company_starter= select_starter(self)
        print(f"            💥 BATALLA INICIAL: {self.player.name} VS {self.human_company} 💥")
        while True:
            if battle(self, self.player.starter, self.company_starter):
                self.locations[0].passed = True
                self.company_starter.psalud, self.company_starter.pdefensa  = 100, 100
                move_location(self, 0)
                break
            self.player.starter.psalud, self.player.starter.pdefensa, self.company_starter.psalud, self.company_starter.pdefensa  = 100, 100, 100, 100


def main():
    """Inicia el juego"""
    game = Game()
    game.start_game()
main()