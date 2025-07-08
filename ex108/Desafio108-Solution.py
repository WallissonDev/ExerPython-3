from ex108 import money

p = float(input('Digite o preço: R$ '))
print(f'A metade de {money.moeda(p)} é {money.moeda(money.metade(p))}')
print(f'O dobro de {money.moeda(p)} é {money.moeda(money.dobro(p))}')
print(f'Aumento de 10%, é {money.moeda(money.aumentar(p, 10))}')
print(f'Diminuindo em 10%, é {money.moeda(money.diminuir(p, 10))}')