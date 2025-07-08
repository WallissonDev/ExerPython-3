from random import randint
print('GAME: JOKENPO')
print('[0] PEDRA ')
print('[1] PAPEL ')
print('[2] TESOURA ')
lista = ('PEDRA','PAPEL','TESOURA')
jogador = int(input('Escolha: '))
pc = randint(0,2)
print('PC:', lista[pc])
print('Jogador:', lista[jogador])
if pc == 0:
    if jogador == 0:
        print(f'Empate! PC: {pc} JGD: {jogador}')
    elif jogador == 1:
        print(f'Jogador venceu: PC: {pc} JGD: {jogador}')
    elif jogador == 2:
        print(f'Pc venceu!: PC {pc} JGD: {jogador}')
    else:
        print('Invalido')
elif pc == 1:
    if jogador == 0:
        print(f'PC venceu! PC: {pc} JGD: {jogador}')
    elif jogador == 1:
        print(f'Empate! PC: {pc} JGD: {jogador}')
    elif jogador == 2:
        print(f'Jogador Venceu! PC: {pc} JGD: {jogador}')
    else:
        print('Invalido')
elif pc == 2:
    if jogador == 0:
        print(f'Jogador venceu! PC: {pc} JGD: {jogador}')
    elif jogador == 1:
        print(f'PC venceu! PC: {pc} JGD: {jogador}')
    elif jogador == 2:
        print(f'Empate! PC: {pc} JGD: {jogador}')
else:
    print('Invalido')

