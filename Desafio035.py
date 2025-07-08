a = int(input('Digite o tamanho de reta A: '))
b = int(input('Digite o tamanho da reta B: '))
c = int(input('Digite o tamanho da reta C: '))
rA = a + b > c
rB = a + c > b
rC = b + c > a
if rA == rB == rC:
    print('É possível formar um triangulo')
else:
    print('Não é possível formar um triangulo')
