num_fact = int(input('Digite um número: '))
i = num_fact - 1
num = num_fact
soma = 0
print(f'{num_fact}! = ', end = '')
while i > 0:
    soma = i * num
    num = soma
    print(f'x {i}', end=' ')
    i -= 1
print(f' = {num}')