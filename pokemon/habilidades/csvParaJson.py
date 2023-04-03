import json
import csv
listaGolpes = []
with open('movimentos.csv', newline='') as csvfile:
    fieldnamesT = ["Name","Type","Cat","Power","Acc","PP","TM","Effect","Prob"]
    golpes = csv.DictReader(csvfile, fieldnames=fieldnamesT )
    for item in golpes:
        listaGolpes.append(item)
    
with open("movePoke.json", 'w') as habilidade:
        json.dump(listaGolpes, habilidade, indent=2)

# converter lista csv para json usando python.
