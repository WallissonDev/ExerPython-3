sal = float(input('Digite o seu salário: '))
valor = float(input('Digite o valor da casa: '))
tempo = int(input('Digite em quantos anos pretendo pagar: '))
mensal = valor / ( 12 * tempo )
salPerc = sal * 30 / 100
if salPerc >= mensal:
    print('Você consegue pagar no prazo determinado')
    print(f'Você terá que pagar mensalmente o valor de R$ {mensal:.2f}')
    print(f'O valor da casa R$ {valor}, mensalmente custa R$ {mensal:.2f} ')
    print(f'Seu salário de R$ {sal}, sendo retirado 30% no valor de R$ {salPerc}')
    print(f'Levará {tempo} mêses pra pagar.')
    print(f'Levara {tempo*12} anos pra pagar')
elif salPerc < mensal:
    print(f'Você não consegue pagar pois a mensalidade da casa é de R$ {mensal:.2f}')
    print(f'Isso é superior a 30% do seu salário de R$ {sal}, pois 30% dele representa R$ {salPerc}')
