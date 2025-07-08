produto = str(input('Qual nome do produto : '))
preço = float(input('Qual o valor do produto: '))
maior = 0
barato = preço
caro = preço
nome = produto
total = preço
while True:
    continuar = str(input('Quer continuar? [S N]: ')).upper().strip()[0]
    if continuar in 'SN':
        break
if preço > 1000:
    maior = +1
if continuar == 'S':
    while True:
        print('-'*20)
        produto = str(input('Qual nome do produto : '))
        preço = float(input('Qual o valor do produto: '))
        total += preço
        if preço > caro:
            caro = preço
        elif preço < barato:
            barato = preço
            nome = produto
        if preço > 1000:
            maior += 1
        while True:
            continuar = str(input('Quer continuar? [S N]: ')).upper().strip()[0]
            if continuar in 'SN':
                break
        if continuar == 'N':
            break
elif continuar == 'N' and preço > 1000:
    maior = +1
print(f'O nome do produto mais barato é {nome} seu valor é de R$ {barato}')
print(f'O número de protudos que custam mais de R$ 1.000,00 são {maior}')
print(f'O total de gastos foi de R$ {total}')