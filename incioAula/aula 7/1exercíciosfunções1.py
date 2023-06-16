def linhas(n):
    for i in range(n):
        i += 1
        print(str(i) * i)


valor = int(input("Insira um valor para o número de linhas: "))

linhas(valor)
