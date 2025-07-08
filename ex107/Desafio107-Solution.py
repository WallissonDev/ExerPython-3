from ex107 import money

p = float(input('Digite o preço: R$ '))
print(f'A metade de {p} é {money.metade(p)}')
print(f'O dobro de {p} é {money.dobro(p)}')
print(f'Aumento de 10%, é {money.aumentar(p, 10)}')
print(f'Diminuindo em 10%, é {money.diminuir(p, 10)}')