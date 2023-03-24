class Conta:
    def __init__(self, saldo, numeroConta):
        self._saldo = saldo
        self._numeroConta = numeroConta

    def getSaldo(self):
        return self._saldo

    def setSaldo(self,entradaSaldo):
        if entradaSaldo < 0:
            print("Insira um valor positivo")
        else:
            self._saldo += entradaSaldo
            
    def getNumeroConta(self):
        return self._numeroConta
    
    def setNumeroConta(self,novoNumero):
        self._numeroConta = novoNumero

fulano = Conta(600,556677)
beltrano = Conta(1200,112233)
cicrano = Conta(1000,778899)

print("Fulano")
print(fulano.getNumeroConta(), fulano.getSaldo())
print("Beltrano")
print(beltrano.getNumeroConta(), beltrano.getSaldo())
print("Cicrano")
print(cicrano.getNumeroConta(), cicrano.getSaldo())

fulano.setNumeroConta(787878)
fulano.setSaldo(1400)

beltrano.setNumeroConta(999999)
beltrano.setSaldo(-1400)

cicrano.setNumeroConta(222222)
cicrano.setSaldo(800)

print("Fulano")
print(fulano.getNumeroConta(), fulano.getSaldo())
print("Beltrano")
print(beltrano.getNumeroConta(), beltrano.getSaldo())
print("Cicrano")
print(cicrano.getNumeroConta(), cicrano.getSaldo())

