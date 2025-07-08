import math
rA = int(input('Digite o tamanho da reta A: '))
rB = int(input('Digite o tamanho da reta B: '))
rC = int(input('Digite o tamanho da reta C: '))
if rA == rB == rC:
    print('É um Triangulo Equilátero')
elif rA == rB or rB==rC or rC == rA:
    print('É um Triangulo Isósceles')
else:
    print('É um Triangulo Escaleno')