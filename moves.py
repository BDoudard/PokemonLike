# LES ATTAQUES ET LEURS DIFFERENTS PARAMETRES

from pokemon_types import FEU, EAU, PLANTE, TERRE, NORMAL
from pokemon_types import type_advantage

class Moves:
    def __init__(self, name, type, damages):
        self.name = name
        self.type = type
        self.damages = damages

    def attack_on(self, from_player, to_pnj):
        print(f"{from_player.name} lance l'attaque {self.name} !")

        advantage = type_advantage(self.type, to_pnj.type)
        total_attack = self.damages + from_player.type.buffAtt + advantage - to_pnj.type.buffDef
        total_attack = max(total_attack, 0) # pour que les dégats ne soient pas négatifs

        to_pnj.pv = max(0, to_pnj.pv - total_attack) # pour que les pv du pnj ne soient pas négatifs

        if advantage > 0:
            print("C'est super efficace")       
        elif advantage < 0:
            print("Ce n'est pas très efficace")
        print(f"{to_pnj.name} perd {total_attack} PV !")
        print(f"{to_pnj.name} a maintenant {to_pnj.pv} PV restant.")

# ATTAQUES DISPONIBLES
LANCE_FLAMME = Moves("Lance Flamme", FEU, 75)
INCENDIE = Moves("Incendie", FEU, 40 )
LANCE_EAU = Moves("Lance eau", EAU, 75)
INNONDATION = Moves("Innondation", EAU, 45)
LANCE_PLANTE = Moves("Lance plante", PLANTE, 75)
MOISSONAGE = Moves("Moissonage", PLANTE, 50)
LANCE_TERRE = Moves("Lance terre", TERRE, 75)
TUNNEL = Moves("Tunnel", TERRE, 40)
UPPERCUT = Moves("Uppercut", NORMAL, 35)
NIPPON = Moves("Nippon", NORMAL, 35)
HIGH_KICK = Moves("High Kick", NORMAL, 30)
BALAYETTE = Moves("Balayette", NORMAL, 30)