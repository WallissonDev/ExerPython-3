# Forma 1
#n1 = float(input('Qual seu salário atual: R$ '))
#n2 = (n1*115)/100
#print(f'Seu novo salário com um aumento de 15% é de: R${n2:.2f}')
# Forma 2
n1 = float(input('Qual o seu salário: R$ '))
n2 = n1*15/100
n3 = n1+n2
print(f'Seu salário de R$ {n1:.2f} recebeu um reajuste de 15% ficando R${n3:.2f}')
print(f'O valor representa aumento de R${n2:.2f}')
# Outra possível forma de fazer isso é n2 = n1+(n1*15/100)
# Optei por fazer de outra forma pra também ter separadamente o valor de quanto é 15%
