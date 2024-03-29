def base_datos():
    return {
    "Criaturas": [
        {"Name": "Pikachu", "Id": 1, "Ataques": [1, 2, 3], "Starter": True, "Ubicaciones": [1, 2]},
        {"Name": "Bulbasaur", "Id": 2, "Ataques": [4, 5, 6], "Starter": True, "Ubicaciones": [1, 3]},
        {"Name": "Charmander", "Id": 3, "Ataques": [7, 8, 9], "Starter": True, "Ubicaciones": [4, 5]},
        {"Name": "Squirtle", "Id": 4, "Ataques": [10, 11, 12], "Starter": False, "Ubicaciones": [4, 6]},
        {"Name": "Jigglypuff", "Id": 5, "Ataques": [13, 14, 15], "Starter": False, "Ubicaciones": [7, 8]},
        {"Name": "Meowth", "Id": 6, "Ataques": [16, 17, 18], "Starter": False, "Ubicaciones": [7, 9]},
        {"Name": "Psyduck", "Id": 7, "Ataques": [19, 20, 21], "Starter": False, "Ubicaciones": [10, 11]},
        {"Name": "Geodude", "Id": 8, "Ataques": [22, 23, 24], "Starter": False, "Ubicaciones": [10, 12, 21]},
        {"Name": "Machop", "Id": 9, "Ataques": [25, 26, 24], "Starter": False, "Ubicaciones": [13, 14]},
        {"Name": "Abra", "Id": 10, "Ataques": [23, 22, 21], "Starter": False, "Ubicaciones": [13, 15, 19]},
        {"Name": "Gastly", "Id": 11, "Ataques": [20, 19, 18], "Starter": False, "Ubicaciones": [16, 17]},
        {"Name": "Onix", "Id": 12, "Ataques": [17, 16, 15], "Starter": False, "Ubicaciones": [16, 18, 21]},
        {"Name": "Drowzee", "Id": 13, "Ataques": [1, 5, 10], "Starter": False, "Ubicaciones": [19, 20, 21]}
    ],

    "Ataques": [
        {"Name": "Pisoton", "Psalud": 10, "Pdefensa": 25, "Id": 1},
        {"Name": "Electroshock", "Psalud": 15, "Pdefensa": 20, "Id": 2},
        {"Name": "Thunderbolt", "Psalud": 40, "Pdefensa": 15, "Id": 3},
        {"Name": "Vine Whip", "Psalud": 15, "Pdefensa": 20, "Id": 4},
        {"Name": "Razor Leaf", "Psalud": 10, "Pdefensa": 15, "Id": 5},
        {"Name": "Solar Beam", "Psalud": 35, "Pdefensa": 10, "Id": 6},
        {"Name": "Ember", "Psalud": 15, "Pdefensa": 20, "Id": 7},
        {"Name": "Fire Spin", "Psalud": 10, "Pdefensa": 15, "Id": 8},
        {"Name": "Flamethrower", "Psalud": 35, "Pdefensa": 10, "Id": 9},
        {"Name": "Bubble", "Psalud": 10, "Pdefensa": 5, "Id": 10},
        {"Name": "Water Gun", "Psalud": 15, "Pdefensa": 10, "Id": 11},
        {"Name": "Hydro Pump", "Psalud": 20, "Pdefensa": 10, "Id": 12},
        {"Name": "Sing", "Psalud": 10, "Pdefensa": 5, "Id": 13},
        {"Name": "Disable", "Psalud": 20, "Pdefensa": 10, "Id": 14},
        {"Name": "Dream Eater", "Psalud": 10, "Pdefensa": 10, "Id": 15},
        {"Name": "Scratch", "Psalud": 10, "Pdefensa": 25, "Id": 16},
        {"Name": "Fury Swipes", "Psalud": 15, "Pdefensa": 10, "Id": 17},
        {"Name": "Slash", "Psalud": 20, "Pdefensa": 5, "Id": 18},
        {"Name": "Confusion", "Psalud": 20, "Pdefensa": 15, "Id": 19},
        {"Name": "Psybeam", "Psalud": 10, "Pdefensa": 10, "Id": 20},
        {"Name": "Psychic", "Psalud": 15, "Pdefensa": 15, "Id": 21},
        {"Name": "Rock Throw", "Psalud": 15, "Pdefensa": 20, "Id": 22},
        {"Name": "Magnitude", "Psalud": 10, "Pdefensa": 15, "Id": 23},
        {"Name": "Earthquake", "Psalud": 10, "Pdefensa": 10, "Id": 24},
        {"Name": "Karate Chop", "Psalud": 15, "Pdefensa": 20, "Id": 25},
        {"Name": "Low Kick", "Psalud": 10, "Pdefensa": 15, "Id": 26}
    ],
    
    "Ubicaciones": {
                    "Ruta": [
                    {"Name": "Ruta 1", "Lider Name": None, "Criaturas": [1], "Id": 2},
                    {"Name": "Ruta 2", "Lider Name": None, "Criaturas": [2], "Id": 3},
                    {"Name": "Ruta 3", "Lider Name": None, "Criaturas": [3], "Id": 5},
                    {"Name": "Ruta 4", "Lider Name": None, "Criaturas": [4], "Id": 6},
                    {"Name": "Ruta 5", "Lider Name": None, "Criaturas": [5], "Id": 8},
                    {"Name": "Ruta 6", "Lider Name": None, "Criaturas": [6], "Id": 9},
                    {"Name": "Ruta 7", "Lider Name": None, "Criaturas": [7], "Id": 11},
                    {"Name": "Ruta 8", "Lider Name": None, "Criaturas": [8], "Id": 12},
                    {"Name": "Ruta 9", "Lider Name": None, "Criaturas": [9], "Id": 14},
                    {"Name": "Ruta 10", "Lider Name": None, "Criaturas": [10], "Id": 15},
                    {"Name": "Ruta 11", "Lider Name": None, "Criaturas": [11], "Id": 17},
                    {"Name": "Ruta 12", "Lider Name": None, "Criaturas": [12], "Id": 18},
                    {"Name": "Ruta 13", "Lider Name": None, "Criaturas": [13], "Id": 20}
                    ],
                
                     "Pueblo": [
                            {"Name": "Pueblo Rojo", "Lider Name": "Lino", "Criaturas": [1, 2], "Id": 1},
                            {"Name": "Pueblo Azul", "Lider Name": "Misty", "Criaturas": [3, 4], "Id": 4},
                            {"Name": "Pueblo Amarillo", "Lider Name": "Lt. Surge", "Criaturas": [5, 6], "Id": 7},
                            {"Name": "Pueblo Verde", "Lider Name": "Erika", "Criaturas": [7, 8], "Id": 10},
                            {"Name": "Pueblo Rosa", "Lider Name": "Sabrina", "Criaturas": [9, 10], "Id": 13},
                            {"Name": "Pueblo Morado", "Lider Name": "Koga", "Criaturas": [11, 12], "Id": 16},
                            {"Name": "Pueblo Gris", "Lider Name": "Blaine", "Criaturas": [13, 10], "Id": 19}
                        ],
                        
                     "Liga": [
                            {"Name": "Liga", "Lider Name": "Edel", "Criaturas": [8, 12, 13], "Id": 21}
                        ]
    }}