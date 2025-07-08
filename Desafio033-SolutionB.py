a = int(input('Digite um valor: '))
b = int(input('Digite outro valor: '))
c = int(input('Digite mais um valor: '))
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print(menor)
print(maior)
