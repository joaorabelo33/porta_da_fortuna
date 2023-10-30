

from random import *


print('''
****************************************      
        BEM VINDO AO GAME 21
      
Objetivo do jogo:
-Pedir uma carta aleatória
-Conseguir 21 pontos na soma das cartas
-Cada carta tem um valor de 1 a 10
            BOM GAME!!!'''
)

total_numeros_jogador = 0
while True:
    numero_gerado = randint(1,10)

    print(f'Sua carta foi de numero {numero_gerado}')
    total_numeros_jogador += numero_gerado

    if(total_numeros_jogador > 21):
        print(f'total de pontos: {total_numeros_jogador} que azar!')

        resposta = input('Deseja jogar novamente? s/n').lower()
        if(resposta == 'n'):
            break
        elif(resposta != 'n'):
            total_numeros_jogador = 0
            continue
    elif(total_numeros_jogador < 21):
        print(f'Valor total das cartas {total_numeros_jogador}!')
        resposta = input('Gostaria de somar mais uma carta? (s/n)').lower()
        if(resposta == 'n'):
            break
        elif(resposta != 'n'):
            continue
    elif(total_numeros_jogador == 21):
        print('Parabéns')
        resposta = input('Deseja jogar novamente? s/n').lower()
        if(resposta == 'n'):
            break
        elif(resposta != 's'):
            total_numeros_jogador = 0
            continue

print('Obrigado por jogar')