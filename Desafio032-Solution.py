from datetime import date
yearS = int(input('Que ano quer analisar? se for o atual digite 0: '))
if yearS == 0:
    yearS = date.today().year
if yearS % 4 == 0 and yearS % 100 != 0 or yearS % 400 == 0:
    print(f'O ano é bissexto: {YearS}')
else:
    print(f'O ano não é bissexto: {yearS}')
