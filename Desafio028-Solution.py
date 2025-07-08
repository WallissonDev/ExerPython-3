from time import sleep
from random import randint
print('--=--'*10)
print('Vou pensar em um número de 0 a 5... adivinhe!')
print('--=--'*10)
robot = int(input('Que número pensei? '))
print('Processando...')
sleep(2)
number = randint(0,5)
if robot == number:
    print(f'Acertou! pensei em {robot}')
else:
    print(f'Errou! pensei em {number}')
