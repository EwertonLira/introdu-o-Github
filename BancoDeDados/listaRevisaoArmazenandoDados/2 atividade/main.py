from os import system 
import json
caminho = "listaRevisaoArmazenandoDados/2 atividade/saldo.json"

class Banco():
    def __init__(self,saldo=None):
        if saldo:
            self._saldo = saldo
        else:
            self._saldo = retomarSaldoDoJson()
    
    def getSaldo(self):
        return self._saldo

    def setDepositar(self,valorRecebido):
        
        if valorRecebido <= 0:
            print("o valor depositado não pode ser negativo ou zero")
            valorBoleano = False
        else:
            self._saldo += valorRecebido
            valorBoleano = True

        return valorBoleano

    def setSacar(self,valorRetirado):
        if valorRetirado <= 0:
            valorRetirado = -1 * valorRetirado # se for negativo a entrada de dados, então vai ficar positivo

        saldo = self._saldo - valorRetirado
        if saldo < 0:
            print("não é possível sacar esse valor da sua conta. verifique o seu saldo")
            valorBoleano = False
        else:
            self._saldo -= valorRetirado
            valorBoleano = True
        
        return valorBoleano


def salvarSaldoNoJson(saldo):    
    # abrir o arquivo saldo.json e salvar o valor do saldo.

    with open(caminho, "w") as saldoJson:
        json.dump(saldo,saldoJson,indent=2) #"saldo" o arquivo que vai ser gravado,"saldoJson" onde vai ser gravdo,"indent=" como vai ser organizado

def retomarSaldoDoJson():
    # abrir o arquivo saldo.Json e pegar o valor que está no arquivo.

    with open(caminho,"r") as saldojson:
        saldoJson = json.load(saldojson)
    
    return saldoJson

#conta criada
user = Banco() # criado sem valor para pegar o saldo direto do arquivo json

while True:
    # início menu principal
    print("\nEssa é sua conta bancária.\nEscolha uma das opções abaixo:\n\t[A] Saldo\n\t[S] sacar\n\t[D] depositar\n\t[F] sair")
    opcao =  input(": ")
    # fim menu principal

    # inicio opções do menu
    match opcao:
        case "a" | "A":
            valor = user.getSaldo() # mostra o saldo
            print(f"o seu é de {valor:.2f}")
        
        case "s" | "S":
            try:
                valor = float(input("Digite o valor do saque: "))
                deuCerto = user.setSacar(valor)
                if deuCerto:
                    print(f"foi sacado o valor de {valor:.2f} da sua conta")
                    salvarSaldoNoJson(user.getSaldo())
            except:
                print("somente números. Tente novamente")
        
        case "d" | "D":
            try:
                valor = float(input("Digite o valor do depósito: "))
                deuCerto = user.setDepositar(valor)
                if deuCerto:
                    print(f"foi depositado o valor de {valor:.2f} da sua conta")
                    salvarSaldoNoJson(user.getSaldo())
            except:
                print("somente números. Tente novamente")
       
        case "f" | "F":
            opcaoSN = input("Tem certeza?\n[S]sim ou [N]não: ")
            match opcaoSN:
                case "s" | "S":
                    print("obrigado por usar")
                    break
                case "n" | "N":
                    print("voltando ao menu")
                    input("Pressione Enter para continuar")
                case _:
                    print("comando inválido")
        
        case _:
                    print("comando inválido")
    # fim opções do menu

    # fim de qualquer opção do menu
    input("Pressione Enter para continuar")
    system("cls")

