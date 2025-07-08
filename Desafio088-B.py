from random import randint
from time import sleep
num = list()
temp = list()
cont = 0
while True:
    jogos = int(input('Quantos jogos quer gerar? '))
    if jogos == 1:
        while cont != 6:
            palpite = randint(1,60)
            if palpite not in num:
                num.append(palpite)
                cont += 1
        sleep(1)
        print(f'Jogo 1: {num}')
    else:
        for c in range(0 , jogos):
            for p in range(1,7):
                palpite = randint(1,60)
                temp.append(palpite)
            num.append(temp[:])
            temp.clear()
            sleep(1)
            print(f'Jogo {c+1}: {num[c]}')
    num.clear()
    while True:
        continuar = str(input('Quer continuar? [S-N]: ')).upper().strip()[0]
        if continuar in 'NnSs':
            break
    if continuar in 'Nn':
        break


