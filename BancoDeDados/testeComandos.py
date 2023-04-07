
def listasAninhadas():
    # 3. navegar pela tabela
    tabela = [("l0","Ewerton","não"),("l1","Rafael","não"),("l2","Miguel","não")]

    for l in tabela:
        id_autor = l[0][1]
        nome = l[1]
        _vazio = l[2]

        print( id_autor ,nome)

    # as ultimas varáveis que ficam no loop permanecem. 
    print( id_autor ,nome,_vazio)


