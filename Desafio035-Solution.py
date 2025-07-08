a = float(input('Digite segmento A: '))
b = float(input('Digite segmento B: '))
c = float(input('Digite segmento C: '))
if a + b > c and b + c > a and c + a > b:
    print('Forma um triangulo')
else:
    print('Não forma um triangulo')
