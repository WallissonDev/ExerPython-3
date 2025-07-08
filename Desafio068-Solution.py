from random import randint
c = 0
while True:
    pc = randint(1,10)
    pl = int(input('Qual número? '))
    total = pc+pl
    pi = ' '
    while pi not in 'PI':
        pi = str(input('Par ou Impar? [P - I] ')).upper().strip()[0]
    if pi in 'Pp':
        if total % 2 == 0:
            print(f'Você venceu! Escolheu: {pi+'ar'}! o total foi {total}!')
            c += 1
        else:
            print(f'Você perdeu! teve vitórias consecutivas: {c} ')
            print(f'A soma foi o meu {pc} e o seu {pl} = {total}')
            break
    elif pi in 'Ii':
        if total % 2 == 1:
            print(f'Você venceu! Escolheu: {pi+'mpar'}! o total foi {total}!')
            c += 1
        else:
            print(f'Você perdeu! teve vitórias consecutivas: {c} ')
            print(f'A soma foi o meu {pc} e o seu {pl} = {total}')
            break
    print('Vamos jogar novamente!')
print('GAME OVER')
