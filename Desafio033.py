import math
x = int(input('Digite um número: '))
y = int(input('Digite outro número: '))
z = int(input('Digite mais um número: '))
quest = min(x, y, z)
quest2 = max(x, y, z)
if quest:
    print(f'O menor número é : {quest}')
    print(f'O maior é: {quest2}')

