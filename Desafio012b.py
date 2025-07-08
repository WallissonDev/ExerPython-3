# Forma 1
#n = float(input('Qual o preço do produto: '))
#n2 = (n*95)/100
#print(f'O novo preço do produto com 5% de desconto é {n2}')
# Forma 2
n = float(input('Qual o preço do produto: R$ '))
n2 = n*5/100
n3 = n-n2
print(f'O produto recebendo 5% de desconto custará: R${n3:.2f} o valor do desconto foi R${n2:.2f}')