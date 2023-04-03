
from os import system, name 
from time import sleep 

#9 incluir uso de pelo menos 1 funão fora das clases (feito)
def calculoDeDano(level,spAttack,atkPower,spDefense,stab,weaknessResistance,critical,other,margin):
    
    # level de ambos os pokemons? (caso naõ entender, necessário usar média)
    # spAttack = ataque especial
    # atkPower = base power (bP) = o pontos do dano do movimento
    # spDefense = defesa especial do pokemom que vai receber o golpe.
    # stab = bônus de golpe do mesmo tipo (Same-Type Attack Bônus)
    # weaknessResistance = é a variável de fraqueza ou resistência do defensor, que pode ser entre 0, 0,25, 0,5, 1, 2 e 4;
    # critical = é o valor para critical hits; seu valor será 1,5 para golpes críticos e 1 para golpes normais.
    # other = é a variável para itens, habilidades, efeito de Burn, etc. O valor que você vai colocar dependerá da situação. Por exemplo, você colocaria x1,3 (30%) caso o atacante estivesse segurando Life Orb.
    # margin = é uma variável de margem de erro; se quiser o dano mínimo que este golpe causará, use 80. Para o máximo, use 100.
        
    level = float(level)
    spAttack = float(spAttack)
    atkPower = float(atkPower)
    spDefense = float(spDefense)
    stab = float(stab)
    weaknessResistance = float(weaknessResistance)
    critical = float(critical)
    other = float(other)
    margin = float(margin)
    
    dano = (((2*level/5+2)*(spAttack*atkPower/spDefense)/50)+2)*stab*weaknessResistance*critical*other*(margin/100)
    return dano

def limparTela(): 
    
    if name == 'nt': 
        _ = system('cls') 
      
    else: 
        _ = system('clear') 
