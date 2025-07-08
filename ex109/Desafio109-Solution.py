from ex109 import money

p = float(input('Digite o preço: R$ '))
print(f'A metade de {money.moeda(p)} é {money.metade(p, True)}')
print(f'O dobro de {money.moeda(p)} é {money.dobro(p, True)}')
print(f'Aumento de 10%, é {money.aumentar(p, 10, True)}')
print(f'Diminuindo em 10%, é {money.diminuir(p, 10, True)}')