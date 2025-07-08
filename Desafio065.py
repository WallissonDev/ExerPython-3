num = int(input('Digite um valor : '))
c = 1
continuar = str(input('Quer continuar? [S/N] : '))[0].upper().split()
soma = num
while continuar != ['N']:
    num = int(input('Digite um valor : '))
    continuar = str(input('Quer continuar? [S/N] : '))[0].upper().split()
    print(continuar)
    soma += num
    c += 1
    if continuar != ['S'] and continuar != ['N']:
        print('Resposta Inválida!')
        soma -= num
        c -= 1
print(f' A soma total é de {soma} a média é {soma/c}')


