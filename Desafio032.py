import calendar
yearS = int(input('Digite o ano: '))
subYear = calendar.isleap(yearS)
if subYear:
    print(f'O ano {yearS} é bissexto!')
else:
    print(f'O ano {yearS} não é bissexto')