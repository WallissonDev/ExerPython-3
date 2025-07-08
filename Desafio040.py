wwnoteOne = float(input('Digite sua primeira nota: '))
noteTwo = float(input('Digite sua segunda nota: '))
media = ( noteOne + noteTwo ) / 2
if media <= 5.0:
    print(f'Infelizmente sua nota foi {media} e foi reprovado!')
elif media >= 7.0:
    print(f'Parabéns! Sua noite foi {media}, você foi aprovado!')
elif media >= 5.9 or media >= 6.9:
    print(f'Foi quase você está de recuperação com a média em {media}')

