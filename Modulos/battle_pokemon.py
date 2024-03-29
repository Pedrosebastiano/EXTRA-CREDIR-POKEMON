#IMPORTACION DE LIBRERIAS
from random import randint
#IMPORTACION DE MODULOS
from Objetos.location import Ruta, Pueblo, Liga


def move_location(self, index):
    """Funcion que permite moverse a las ubicaciones anteriores o siguientes, dependiendo del tipo de ubicacion
    muestra menus diferentes
    No retorna, se ejecuta hasta ganar al lider de liga"""
    first_time = False
    while True:
        print(f"     🗺️ Actualmente se encuentra en {self.locations[index].name}")
        if index:
            option = input(f"""\n           Seleccione la option que desee hacer:
                        1. Ir a {self.locations[index + 1].name}
                        2. Regresar a {self.locations[index - 1].name}
                        >>> """)
        else:
            option = input(f"""           Seleccione la option que desee hacer:
                        1. Ir a {self.locations[index + 1].name}
                        >>> """)
        if option == "1":
            if self.locations[index].passed:
                index += 1
            else:
                print("\n          Debe vencer la ruta primero 🗡️\n")
                move_location(self, index)
        elif option == "2":
            index -= 1
        else:
            print("\n             Ingrese Invalido!!!❌\n")
        if isinstance(self.locations[index], Ruta):
            if randint(0, 1):
                if battle(self, self.player.starter, self.locations[index].creatures[0]):
                    self.locations[index].passed = True
            else:
                self.locations[index].passed = True
        elif isinstance(self.locations[index], Pueblo):
            while True:
                if first_time:
                    option = input(f"""           Seleccione la option que desee hacer:
                        1. Enfrentar al Lider
                        2. Sanar starter
                        3. Seguir rutas
                        >>> """)
                    if option == "1":
                        if battle(self, self.player.starter, self.locations[index].creatures[0]):
                            if battle(self, self.player.starter, self.locations[index].creatures[1]):
                                print(f"\n             🥳Felicidades usted ha VENCIDO a la {self.locations[index].lider_name} 🥳")
                                self.locations[index].passed = True
                    elif option == "2":
                        heal(self.player.starter)
                    elif option == "3":
                        if self.locations[index].passed:
                            break
                        else:
                            print("\n          Debe vencer al lider primero 🗡️\n")
                    else:
                        print("\n             Ingrese Invalido!!!❌\n")
                else:
                    break
        elif isinstance(self.locations[index], Liga):
            while True:
                if first_time:
                    option = input(f"""           Seleccione la option que desee hacer:
                        1. Enfrentar al Lider
                        2. Sanar starter
                        >>> """)
                    if option == "1":
                        if battle(self, self.player.starter, self.locations[index].creatures[0]):
                            if battle(self, self.player.starter, self.locations[index].creatures[1]):
                                if battle(self, self.player.starter, self.locations[index].creatures[2]):
                                    print("------------------------------------------------------------------")
                                    print(f"            🎊🎉FELICIDADES {self.player.name} USTED SE HA PASADO EL JUEGO🎉🎊")
                                    while True:
                                        print("                 Presione enter para cerrar el programa ↩️")
                                        close = input("")
                                        if not(close):
                                            print(f"                    HASTA LUEGO👋")
                                            break
                                    quit()
                    elif option == "2":
                        heal(self.player.starter)
                    else:
                        print("\n             Ingrese Invalido!!!❌\n")
                else:
                    break
            break
        first_time = True
    

def battle(self, pokemon1, pokemon2):
    """Funcion que permite realizar batallas entre 2 pokemones que recibe como parametro, pide por teclado el ataque
    y realiza el ataque oponente de manera aleatoria
    Retorna True en caso de ganar la batalla, y False si se pierde. En caso de empate, se realiza nuevamente la batalla"""
    print("------------------------------------------------------------------")
    print(f"\n                  🛡️ BATALLA INICIADA 🛡️\n")
    print(f"                  🤜 {pokemon1.name} VS {pokemon2.name} 🤛\n")
    print("------------------------------------------------------------------\n")
    if pokemon1.psalud > 0:
        s_pokemon2 = 100
        d_pokemon2 = 100
        while pokemon1.psalud > 0 and s_pokemon2 > 0:
            #TURNO DEL JUGADOR
            cont = 1
            for ataque in pokemon1.attacks:
                print(f"            {cont}. {ataque.name}👊")
                cont += 1
            try: 
                selec = int(input("             🤜Ingrese el numero del ataque que hara>>>"))
                if selec > len(pokemon1.attacks):

                    raise Exception
            except:
                print("\n             Ingreso Invalido!!!❌\n")
                continue
            print(f"""\n            💥Ha atacado con {pokemon1.attacks[selec-1].name}💥
                           🩺-{pokemon1.attacks[selec-1].ps_oponente}🩺
                           🛡️  -{pokemon1.attacks[selec-1].pd_oponente}🛡️""")
            s_pokemon2 -= pokemon1.attacks[selec-1].ps_oponente
            d_pokemon2 -= pokemon1.attacks[selec-1].pd_oponente
            #TURNO DEL OPONENTE
            selec_oponent = randint(0, len(pokemon2.attacks) - 1)
            print(f"""\n            💥El oponente atacado con {pokemon2.attacks[selec_oponent].name}💥
                           🩺-{pokemon2.attacks[selec_oponent].ps_oponente}🩺
                           🛡️  -{pokemon2.attacks[selec_oponent].pd_oponente}🛡️""")
            pokemon1.psalud -= pokemon2.attacks[selec_oponent].ps_oponente
            pokemon1.pdefensa -= pokemon2.attacks[selec_oponent].pd_oponente


        if pokemon1.psalud <= 0 and s_pokemon2 <=0:
            print("             🤝 EMPATE 🗡️")
            pokemon2.psalud, pokemon2.pdefensa, pokemon1.psalud, pokemon1.pdefensa  = 100, 100, 100, 100

            if battle(self, pokemon1, pokemon2):
                return True
            else:
                return False
        elif pokemon1.psalud <= 0:
            print("             😭Usted ha sido DERROTADO 🗡️")
            return False
        elif s_pokemon2 <=0:
            print("             💪Felicidades usted ha GANADO la batalla 🗡️")
            new_attack(self, pokemon1)
            return True
        pokemon2.psalud, pokemon2.pdefensa= 100, 100
        print(pokemon1.win)
        
    else:
        print(f"\n😡 USTED HA SIDO AMONESTADO POR COMENZAR LA BATALLA CON 0 PUNTOS DE SALUD 😡\n")


def new_attack(self, pokemon1):
    """Funcion que permite añadir nuevos ataques a los pokemones, luego de ganar 2 batallas.
    No retorna, añade a la lista de ataques nuevos ataques"""
    if len(pokemon1.attacks)<10:
        pokemon1.win += 1
        if pokemon1.win == 2:
            pokemon1.win = 0
            while True:
                ataque= self.attacks[randint(0, len(self.attacks) -1)]
                if ataque in pokemon1.attacks:
                    continue
                else:
                    pokemon1.attacks.append(ataque)
                    print(f"                Haz conseguido el ataque {ataque.name} 🦍")
                    break


def heal(pokemon):
    """Funcion que permite curar los puntos de vida de los pokemones
    No retorna, fija a 100 ambos puntos del pokemon que recibe"""
    print(f"\n         {pokemon.name} sanado completamente💘\n")
    pokemon.psalud=100
    pokemon.pdefensa=100