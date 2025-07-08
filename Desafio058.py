from random import randint
robot = randint(0,10)
guess = 0
count = 1
while guess != robot:
    guess = int(input('Digite o valor que estou pensando: '))
    if guess != robot:
        print('Errou! Tente novamente!')
        count += 1
    else:
        print(f'Parabéns! pensei em {robot} você levou {count} vezes pra acertar')