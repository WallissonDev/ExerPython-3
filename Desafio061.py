primeiro_termo = int(input('Digite o primeiro termo de uma PA: '))
razao = int(input('Digite a razão da PA: '))
proximo = 0
i = primeiro_termo
dez = primeiro_termo + razao * 10
print(f'PA de {primeiro_termo} com razao de {razao} ---> {i} + {razao} = ', end = ' ')
while proximo < dez:
    proximo = i + razao
    i = proximo
    proximo += razao
    print(f'{i} + {razao} = ', end = ' ')
print(f' = {i+razao}', end = ' ')

