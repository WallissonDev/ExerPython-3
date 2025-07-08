import math
ang = float(input('Digite um angulo: '))
ang2 = math.radians(ang)
se = math.sin(ang2)
co = math.cos(ang2)
ta = math.tan(ang2)
print(f'O Seno é: {se:.2f}\nO Coseno é: {co:.2f}\nA Tangente é: {ta:.2f}')
