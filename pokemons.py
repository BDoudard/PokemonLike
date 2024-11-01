# DEFINITION D'UN POKEMON ET DE SES ATTRIBUTS

from pokemon_types import EAU, FEU, PLANTE, TERRE, NORMAL
from pokemon_types import type_advantage
from moves import *

class Pokemon:
    def __init__(self, name, pv, type, moves):
        self.name = name
        self.pv = pv
        self.type = type
        self.moves = moves 

    def do_moves(self, moves_id, pokemon):
        if 0 <= moves_id < len(self.moves):
            selected_move = self.moves[moves_id]
            selected_move.attack_on(self, pokemon)
        else:
            print("Vous devez sélectionner une attaque.")

    def defense(self, attack, type_attack):
        return attack - self.type.buffDef - (type_advantage(self.type, type_attack))    


# POKEMONS DISPONIBLES 

nekfeu = Pokemon("Nekfeu", 200, FEU, [LANCE_FLAMME, INCENDIE, HIGH_KICK, UPPERCUT])
nekwater = Pokemon("Nekwater", 220, EAU, [LANCE_EAU, INNONDATION, BALAYETTE, NIPPON])
nekplante = Pokemon("Nekplante", 240, PLANTE, [LANCE_PLANTE, MOISSONAGE, UPPERCUT, BALAYETTE])
nekterre = Pokemon("Nekterre", 230, TERRE, [LANCE_TERRE, TUNNEL, NIPPON, HIGH_KICK])

pokedex =   (nekfeu,
    nekwater,
    nekplante,
    nekterre)


