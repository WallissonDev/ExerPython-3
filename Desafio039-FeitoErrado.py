from datetime import datetime, timedelta, date
ano = input('Digite sua data de nascimento YYYYMMDD: ')
conv = datetime(year=int(ano[0:4]), month=int(ano[4:6]), day=int(ano[6:8]))
alist = date.today()
if conv < alist:
    print (f'Você nasceu no dia {conv} e hoje é {alist}')