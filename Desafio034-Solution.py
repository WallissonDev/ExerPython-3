sal = float(input('Digite seu salário: '))
aumten = sal*10 / 100 + sal
aumfit = sal*15 / 100 + sal
if sal >= 1250:
    print('Seu novo salário com aumento de 10% é : ', aumten)
else:
    print('Seu novo salário com aumento de 15% é: ', aumfit)