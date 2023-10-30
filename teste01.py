
from random import *


print('''
Porta da Fortuna!
=========
Existe um super prêmio atrás de uma destas 3 portas!
adivinhe qual é a porta certa para ganhar e!
  _____   _____   _____
 |     | |     | |     |
 | [1] | | [2] | | [3] |
 |   o | |   o | |   o |
 |_____| |_____| |_____|
''')
contador_acertos = 0
for i in range(3):
    print('Escolha uma porta (1, 2 ou 3):')


    porta_escolhida = input()
    porta_escolhida = int(porta_escolhida)


    porta_certa = randint(1,3)


    print("A porta escolhida é", porta_escolhida)
    print("A porta vencedora és", porta_certa)


    if porta_escolhida == porta_certa:
        print("Muito bem!")
        contador_acertos += 1
    else:
        print("Azar!")

print('Total de acertos: ', contador_acertos)