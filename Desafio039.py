from datetime import date
ano = int(input('Digite seu ano de nascimento: '))
current = date.today().year
if current - ano == 18:
    print('Você tem 18 anos, deve se alistar esse ano!')
elif current - ano < 18:
    print(f'Você ainda não deve se alistar, faltam {ano-current+18} anos!')#
elif current - ano > 18:
    print(f'Você já passou da data de se alistar {current-ano-18} em anos!')