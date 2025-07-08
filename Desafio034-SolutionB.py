sal = float(input('Digite seu salário: R$ '))
if sal >= 1250:
    novo = sal + (sal * 10 / 100)
else:
    novo = sal + (sal * 15 / 100)
print('Seu novo salário é: R$' , novo)
