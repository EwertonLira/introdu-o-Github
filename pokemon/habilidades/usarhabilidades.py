import csv
listaGolpes = []
with open('habilidades/movePoke.csv', newline='') as csvfile:
    fieldnamesT = ["indice", 'name','descricao','poder','acertividade','pp']
    golpes = csv.DictReader(csvfile, fieldnames=fieldnamesT )
    
    # for ind,name,golpes,poder,acert,pp in golpes.items():
    #     print(poder)
    for row in golpes:
        listaGolpes.append((row['indice'], row['name'],row['descricao'],row['acertividade'],row['pp']))


print(listaGolpes)