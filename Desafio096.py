def est():
    print('-' * 20)
    print('Controle de Terrenos')
    print('-' * 20)
def area(a,b):
    s = a*b
    print(f'O terreno com largura de {a:.2f}m² e comprimento de {b:.2f}m² tem a área de {s:.2f}m²')
est()
a = float(input('Largura(m): '))
b = float(input('Comprimento(m): '))
area(a,b)