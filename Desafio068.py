from random import randint
pc = 0
jogador = 0
c = 0
while True:
    pc = randint(0,10)
    jogador = int(input('Digite um valor: '))
    pi = str(input('Par ou Impar? [I/P]: ')).upper().strip()[0]
    if pi == 'I' and (pc+jogador) % 2 == 1:
        print(f'Você venceu! Você escolheu {pi+'mpar'} o número {jogador} e eu {pc}!')
        c += 1
    elif pi == 'P' and (pc+jogador) % 2 == 0:
        print(f'Você venceu! Você escolheu {pi+'ar'} o número {jogador} e eu {pc}!')
        c += 1
    else:
        print(f'Você perdeu! escolhi {pc} e você {jogador}!')
        break
print(f'Você teve o total de {c} vitórias')