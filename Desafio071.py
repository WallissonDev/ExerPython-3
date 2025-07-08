valor = int(input('Digite o valor a ser sacado: '))
valor_original = valor
n50 = 0
n20 = 0
n10 = 0
n1 = 0
while True:
    if valor >= 50:
        n50 = valor // 50
        valor = valor % 50
    if valor <= 50:
        n20 = valor // 20
        valor = valor % 20
    if valor <= 20:
        n10 = valor // 10
        valor = valor % 10
    if valor <= 10:
        n1 = valor * 1
        valor -= n1
    if valor == 0:
        break
print(f'O valor digitado foi {valor_original}')
print(f'Notas de R$ 50,00 = Quantia: {n50}')
print(f'Notas de R$ 20,00 = Quantia: {n20}')
print(f'Notas de R$ 10,00 = Quantia: {n10}')
print(f'Notas de R$ 1,00 = Quantia: {n1}')