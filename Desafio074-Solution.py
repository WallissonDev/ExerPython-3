from random import randint
numeros = (randint(0,10),randint(0,10),randint(0,10),
            randint(0,10),randint(0,10))
print(f'Gerei os números:')
for n in numeros:
    print(f'{n} ' , end = '')
print(f'O menor valor foi: {min(numeros)}')
print(f'O maior valor foi: {max(numeros)}')
