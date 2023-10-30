

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
jogando = True
contador_acertos = 0
while jogando:
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
        print("Azar! score zerado")
        contador_acertos = 0


    print('Você quer jogar de novo?')
    resposta = input().lower()
    if resposta == 'n'or resposta == 'nao' or resposta[0]=='n':
        jogando = False
print('obrigado por jogar')
print('Sua pontuação final foi de:', contador_acertos)