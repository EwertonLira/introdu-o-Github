import json
import csv
listaPoke = []
with open('pokemon.csv', newline='') as csvfile:
    fieldnamesT = ["indice","Name","Type 1","Type 2","Total","HP","Attack","Defense","Sp. Atk","Sp. Def","Speed","Generation","Legendary"]
    pokemons = csv.DictReader(csvfile, fieldnames=fieldnamesT )
    for item in pokemons:
        listaPoke.append(item)
    
with open("poke.json", 'w') as pokemon:
        json.dump(listaPoke, pokemon, indent=2)