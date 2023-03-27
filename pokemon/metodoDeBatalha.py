# Criar método de batalha onde dois pokemons, lutam e é determinado o
# vencedor. Os turnos da batalha e seu resultado devem ser impressos no
# terminal. O pokemon do jogador deve ser escolhido pelo próprio com
# base na sua lista de pokemons, o pokemon do Inimigo deve ser escolhido
# aleatoriamente (usar a biblioteca random)

# dar uma olhada
#https://pokemondb.net/move/all


#________________________________

# level de ambos os pokemons? (caso naõ entender, necessário usar média)
# spAttack = ataque especial
# atkPower = base power (bP) = o pontos do dano do movimento
# spDefense = defesa especial do pokemom que vai receber o golpe.
# stab = bônus de golpe do mesmo tipo (Same-Type Attack Bônus)
# weaknessResistance = é a variável de fraqueza ou resistência do defensor, que pode ser entre 0, 0,25, 0,5, 1, 2 e 4;
# critical = é o valor para critical hits; seu valor será 1,5 para golpes críticos e 1 para golpes normais.
# other = é a variável para itens, habilidades, efeito de Burn, etc. O valor que você vai colocar dependerá da situação. Por exemplo, você colocaria x1,3 (30%) caso o atacante estivesse segurando Life Orb.
# margin = é uma variável de margem de erro; se quiser o dano mínimo que este golpe causará, use 80. Para o máximo, use 100.

def calculoDeDano(level,spAttack,atkPower,spDefense,stab,weaknessResistance,critical,other,margin):
    dano = ((((2*level/5+2)*spAttack*atkPower/spDefense)/50)+2)*stab*weaknessResistance*critical*other*(margin/100)
    return dano


def statsModifiers(atributo,levelModificador):   
    match levelModificador:
        case -6:
            valor = -6
        case -5:
            valor = -5
        case -4:
            valor = -4
        case -3:
            valor = -3
        case -2:
            valor = -2
        case -1:
            valor = -1
        case 0:
            valor = 0
        case 1:
            valor = 1
        case 2:
            valor = 2
        case 3:
            valor = 3
        case 4:
            valor = 4
        case 5:
            valor = 5
        case 6:
            valor = 6
    
    resultado = atributo * levelModificador
    return resultado

print(statsModifiers(120,3))