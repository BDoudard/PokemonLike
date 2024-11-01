# LES DIFFERENTS TYPES, ATTRIBUABLES AUX POKEMONS

class Type:
    def __init__(self, name, buffAtt, buffDef):
        self.name = name
        self.buffAtt = buffAtt        
        self.buffDef = buffDef

EAU = Type("EAU", 5, 5)
FEU = Type("FEU", 6, 7)
PLANTE = Type("PLANTE", 4, 7)
TERRE = Type("TERRE", 3, 8)
NORMAL = Type("NORMAL", 0, 0)

# AVANTAGE OU DESAVANTAGE DE TYPE SUR UN AUTRE

def type_advantage(type_att, type_def):
    if type_att.name == "EAU" and type_def.name == "FEU":
        return 20
    elif type_att.name == "FEU" and type_def.name == "PLANTE":
        return 20
    elif type_att.name == "TERRE" and type_def.name == "FEU":
        return 20
    elif type_att.name == "PLANTE" and type_def.name == "TERRE":
        return 20
    elif type_att.name == "PLANTE" and type_def.name == "EAU":
        return 20
    elif type_att.name == "EAU" and type_def.name == "EAU":
        return -40
    elif type_att.name == "FEU" and type_def.name == "FEU":
        return -40
    elif type_att.name == "TERRE" and type_def.name == "TERRE":
        return -40
    elif type_att.name == "PLANTE" and type_def.name == "PLANTE":
        return -40
    else:
        return 0
    