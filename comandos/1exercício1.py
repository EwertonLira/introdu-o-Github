class Triangulo:
    def __init__ (self,ladoA,ladoB,ladoC):
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.ladoC = ladoC

    def calcularPerímetro(self):
        return self.ladoA + self.ladoB + self.ladoC

    def getMaiorLado(self):
            if self.ladoA == self.ladoB and self.ladoA == self.ladoC:
                maiorLado = "três lados são iguais"
            elif self.ladoA == self.ladoB and self.ladoA != self.ladoC:
                maiorLado = f"Dois lados são iguais {self.ladoA}"
            elif self.ladoA > self.ladoB and self.ladoA > self.ladoC:
                maiorLado = self.ladoA
            elif self.ladoB > self.ladoA and self.ladoB > self.ladoC:
                 maiorLado = self.ladoB
            else:
                 maiorLado = self.ladoC
            
            return maiorLado

    def mostrarResultado(self):
        print(f"""
        O perímetro do triângulo é: {self.calcularPerímetro()}
        e o maior lado é: {self.getMaiorLado()}
        """)

lados = []
for item in range(3):
    print(f"insira o valor do {item + 1}° lado:")
    lados.append(int(input(": ")))

triangulo1 = Triangulo(lados[0],lados[1],lados[2])

triangulo1.mostrarResultado()
