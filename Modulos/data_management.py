#IMPORTACION DE MODULOS Y DB
from datos import base_datos
from Objetos.person import Person
from Objetos.pokemon import Pokemon
from Objetos.attacks import Attack
from Objetos.location import Ruta, Pueblo, Liga
#IMPORTACION DE LIBRERIAS
from random import randint


def new_profile(self):
    """Funcion que permite regiustrar el personaje principal, asigna compañero humano
    Retorna objeto persona y compañero humano"""
    while True:
        try:
            name = input("🧑Ingrese su nombre>>>").title()
            age = int(input("🔢Ingrese su edad>>>"))
            cont = 1
            print("     🗺️ UBICACIONES 🗺️\n")
            pueblos = []
            for location in self.locations:
                if isinstance(location, Pueblo):
                    pueblos.append(location)
                    print(f"        {cont}. {location.name}")
                    cont += 1
            origin_place = int(input("📍Ingrese su ubicacion (Numero de la lista)>>>"))
            if origin_place > 7 or origin_place < 0:
                    raise Exception
            print(f"\n       📍Su Pueblo es {pueblos[origin_place-1].name}📍")
            print(f"       🧑 Su compañero humano es {pueblos[origin_place-1].lider_name}🧑\n")
            break
        except:
            print("             \nIngrese Invalido!!!❌\n")
    player = Person(name, age, pueblos[origin_place-1])
    return player, pueblos[origin_place-1].lider_name


def select_starter(self):
    """Funcion que permite seleccionar un starter (Pokemon)
    Retorna al pokemon seleccionado y el pokemon asignado al compañero humano"""
    cont = 1
    print("\n       💪STARTERS💪\n")
    for starter in self.starters:
        print(f"        {cont}. {starter.name}")
        cont += 1

    while True:
        try:
            starter_selected = int(input("          🔢Ingrese el numero del starter que desee>>>"))
            starter_jugador = self.starters[starter_selected - 1]
            if starter_selected > 3 or starter_selected < 0:
                raise Exception
            break
        except:
            print("             Ingrese Invalido!!!❌")
    self.starters.pop(starter_selected - 1)
    starter_human_company = self.starters[randint(0,1)]
    self.starters.append(starter_jugador)
    print(f"\n      ⚡Su Starter es {starter_jugador.name}⚡")
    print(f"       🪵 El starter de su compañero humano es {starter_human_company.name}🪵\n")
    return starter_jugador, starter_human_company


def get_data(self):
    """Funcion que permite crear los objetos pokemon, ataque y ubicacion, tomando los datos del data base
    No retorna, crea listas de objetos"""
    db = base_datos()
    for i, j in db.items():
        if i == "Criaturas":
            for k in j:
                self.creatures.append(Pokemon(k["Name"], k["Starter"], k["Id"], k["Ataques"]))
        elif i == "Ataques":
            for k in j:
                self.attacks.append(Attack(k["Name"], k["Psalud"], k["Pdefensa"], k["Id"]))
        elif i == "Ubicaciones":
            for l, m in j.items():
                for k in m:
                    if l == "Pueblo":
                        self.locations.append(Pueblo(k["Name"], k["Id"], k["Criaturas"], k["Lider Name"]))
                    elif l == "Ruta":
                        self.locations.append(Ruta(k["Name"], k["Id"], k["Criaturas"]))
                    elif l == "Liga":
                        self.locations.append(Liga(k["Name"], k["Id"], k["Criaturas"], k["Lider Name"]))

    for pokemon in self.creatures:
        for ataque in self.attacks:
            if ataque.id in pokemon.ids_ataques:
                pokemon.attacks.append(ataque)
        if pokemon.starter:
            self.starters.append(pokemon)

    for ubicacion in self.locations:
        for pokemon in self.creatures:
            if pokemon.id in ubicacion.ids_pokemones:
                ubicacion.creatures.append(pokemon)


    self.locations = sorted(self.locations, key=lambda location: location.id)