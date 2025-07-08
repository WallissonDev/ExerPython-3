from random import randint
from time import sleep
numeros = list()
def sorteia():
    print('Sorteando 5 valores ', end = '')
    while len(numeros) < 5:
        num = randint(1,50)
        sleep(0.4)
        if num not in numeros:
            numeros.append(num)
            print(num, end = ' ')
    sleep(0.4)
    print(' Pronto!')
    print(f'Os números sorteados foram {numeros}')


def somaPar():
    soma = 0
    for c in numeros:
        if c % 2 == 0:
            soma += c
    print(f'A soma de todos os números pares foi {soma}')


sorteia()
somaPar()
