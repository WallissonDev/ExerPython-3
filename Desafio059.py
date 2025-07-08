escolha = 0
while escolha != 5:
    primeiro = float(input('Digite um valor: '))
    segundo = float(input('Digite outro valor: '))
    print('=' * 30)
    print('MENU ARITMÉTICO')
    print('=' * 30)
    print('[ 1 ] Somar ')
    print('[ 2 ] Multiplicar ')
    print('[ 3 ] Maior ')
    print('[ 4 ] Novos Números ')
    print('[ 5 ] Sair do Programa ')
    escolha = int(input('Escolha: '))
    if escolha == 1:
        soma = primeiro + segundo
        print(f'A soma do {primeiro} com o {segundo} é : {soma}')
    if escolha == 2:
        multiplicação = primeiro * segundo
        print(f'A multiplicação de {primeiro} com {segundo} é {multiplicação}')
    if escolha == 3 and primeiro > segundo:
        maior = primeiro
        print(f'O maior entre eles é {maior}')
    if escolha == 3 and primeiro < segundo:
        maior = segundo
        print(f'O maior entre eles é {maior}')

