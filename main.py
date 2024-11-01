
from pokemons import Pokemon, pokedex
import moves
import random

# APPARITION DU POKEMON ENNEMI
pokemon_pnj = random.choice(pokedex)
print(f"Un {pokemon_pnj.name} sauvage apparait !")
print()

# POKEMONS DISPONIBLES POUR LE JOUEUR
print("Pkémons disponibles : ")       
for i, pokemon in enumerate(pokedex):
    print(f"{i + 1} {pokemon.name}")
print()

# CHOIX DU POKEMON PAR LE JOUEUR
user_pokemon = int(input("Choisissez un Pokémon : ")) -1       
selected_pokemon = pokedex[user_pokemon]
print(f"Vous envoyez {selected_pokemon.name} au combat !")
print()

# COMBAT
while selected_pokemon.pv > 0 and pokemon_pnj.pv > 0:
    # TOUR DU JOUEUR
    print("Attaques disponibles : ")
    for i, move in enumerate(selected_pokemon.moves):
        print(f"{i + 1} {move.name}")
    print()
    
    user_move = int(input("Choisissez une attaque : ")) -1
    if 0 <= user_move < len(selected_pokemon.moves):
        selected_pokemon.do_moves(user_move, pokemon_pnj)

    # SI POKEMON PNJ EST KO
    if pokemon_pnj.pv <= 0:
        print(f"{pokemon_pnj.name} est KO ! Vous gagnez le combat.")
        break

    # TOUR DU PNJ
    print(f"{pokemon_pnj.name} attaque à son tour !")
    pnj_move = random.choice(pokemon_pnj.moves)
    pnj_move.attack_on(pokemon_pnj, selected_pokemon)
    selected_pokemon.pv = max(0, selected_pokemon.pv) # pour que les pv du pokemon du joueur ne soient pas négatifs

    # SI POKEMON JOUEUR EST KO
    if selected_pokemon.pv <= 0:
        print(f"{selected_pokemon.name} est KO ! Vous perdez le combat.")
