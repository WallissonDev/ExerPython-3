prize = float(input('The purchase prize: R$ '))
print('[ 1 ] If you want to pay in money')
print('[ 2 ] If you want to pay in debit')
print('[ 3 ] If you want to pay in credit 2x')
print('[ 4 ] If you want to pay in credit 3x or more')
prize_Method = int(input())
if prize_Method == 1:
    print(f'You have to pay in money R$ {prize-prize*10/100} 10% Descount')
elif prize_Method == 2:
    print(f'You have to pay in debit card R$ {prize-prize*10/100} 10% Descount')
elif prize_Method == 3:
    print('[ 1X ] Write 1: ')
    print('[ 2X ] Write 2: ')
    parcels = int(input())
    if parcels == 1:
        print(f'You have to pay in 1X R$ {prize}')
    elif parcels == 2:
        print(f'You have to pay in 2X of R$ {prize / 2} total of R$ {prize} ')
elif prize_Method == 4:
    print('Write the number of Parcels you want to pay: ')
    parcels = int(input())
    print(f'You have to pay in {parcels}X the prize of R$ {(prize*20/100+prize)/parcels} total of R$ {prize*20/100+prize}')
    print('Fees of 20%')
else:
    print('Invalid Payment Method!')