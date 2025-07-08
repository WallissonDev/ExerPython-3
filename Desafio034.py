value = int(input('Digite seu salário: '))
sal_ten = value*10/100
sal_fiften = value*15/100
if value >= 1250:
    print(f'Seu salário aumentou em 10% ficando R${value + sal_ten:.2f}')
else:
    print(f'Seu salário aumento em 15% ficando R${value + sal_fiften:.2f}')