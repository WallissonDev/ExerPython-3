# Forma 1
#n1 = int(input('Qual a altura da parede: '))
#n2 = int(input('Qual a largura da parede:'))
#n3 = n1*n2
#print(f'A dimensão da sua parede é: {n1}m X {n2}m\nA àrea é {n3}m²\nVocê Precisará de {(n3/(2**2)} litros de tinta para pintar {n3}m² de parede')
# Forma 2
n1 = float(input('Qual a altura da sua parede: '))
n2 = float(input('Qual a largura da sua parede: '))
n3 = n1*n2
n4 = n3/2
print(f'A Area da sua parede é {n1:.1f}x{n2:.1f} ou seja: {n3:.1f}m²\nVocê precisará de {n4}L de tinta.')
