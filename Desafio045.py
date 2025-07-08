import random
from time import sleep
print('\033[1:33mOlá jogador! Vamos jogar Jokenpo!\033[0m')
print('\033[1:32mEscolha Pedra, Papel ou Tesoura!\033[0m')
jogador = str(input('Escolha: ')).upper()
print('Pedra!')
sleep(1)
print('Papel!')
sleep(1)
print('Ou Tesoura!')
sleep(1)
choice1 = 'PAPEL'
choice2 = 'TESOURA'
choice3 = 'PEDRA'
list = [choice1,choice2,choice3]
robot = random.choice(list)
if jogador == robot:
    print(f'EMPATE! Você escolheu: {jogador} e Eu: {robot}')
elif jogador == choice1 and robot == choice2:
    print(f'Eu venci! você escolheu {jogador} e Eu: {robot}')
elif jogador == choice2 and robot == choice3:
    print(f'Eu venci! você escolheu {jogador} e Eu: {robot}')
elif jogador == choice3 and robot == choice1:
    print(f'Eu venci! você escolheu {jogador} e Eu: {robot}')
else:
    print(f'Você venceu! escolheu {jogador} e Eu: {robot}')