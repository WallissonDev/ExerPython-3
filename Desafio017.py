#from math import sqrt
#a = float(input('Qual o cateto oposto: '))
#b = float(input('Qual o cateto adjacente: '))
#c = sqrt(a**2+b**2)
#print(f'O cateto oposto {a} e o cateto adjacente {b} resultam na hipotenusa {c:.2f}cm²')
#
#No modulo math tem o hypot que representa a hipotenusa
#
#from math import hypot
#ca = float(input('Qual o cateto adjacente:'))
#co = float(input('Qual o cateto oposto: '))
#hi = hypot(ca,co)
#print(f'A hipotenusa é: {hi}')
#
import math
ca = float(input('Qual o cateto adjacente: '))
co = float(input('Qual o cateto oposto: '))
hi = math.hypot(ca,co)
print(f'A hipotenusa é {hi:.2f}')