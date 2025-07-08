import datetime
idade = int(input('Digite seu ano de Nascimento: '))
data = datetime.date.today().year
if data - idade <= 9:
    print('Sua categoria é Mirim')
elif data - idade <= 14:
    print('Sua categoria é Infantil')
elif data - idade == 19:
    print('Sua categoria é Junior')
elif data - idade == 20:
    print('Sua categoria é Senior')
elif data - idade > 20:
    print('Sua categoria é Master')

