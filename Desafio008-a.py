# Forma 1
# n1 = int(input('Escreva um valor:'))
# print(f'O valor {n1}m em centrimetros é {n1*100}cm em milimetros {n1*1000}mm')
# Forma 2

n1 = float(input('Digite um valor em metros: '))
n2 = n1/1000
n3 = n1*100
n4 = n1*1000
print(f'O valor em metros {n1} m\n{n2:.2f} Km\n{n3} Cm\n{n4} mm')