print(f'{'WallyShopee':=^40}')
price = float(input('The purchase prize: R$ '))
print('[ 1 ] If you want to pay in money')
print('[ 2 ] If you want to pay in debit')
print('[ 3 ] If you want to pay in credit 2x')
print('[ 4 ] If you want to pay in credit 3x or more')
method = int(input())
if method == 1:
    finalPrice = price - (price * 10 / 100)
    print(f' Your price will be R$ {finalPrice}')
elif method == 2:
    finalPrice = price - (price * 5 / 100)
    print(f' Your price will be R$ {finalPrice}')
elif method == 3:
    finalPrice = price
    parcels = finalPrice / 2
    print(f'You have to pay R$ {finalPrice} in 2x of {parcels}')
elif method == 4:
    finalPrice = price + ( price * 20 / 100)
    numParcels = int(input('Number of parcels: '))
    totalPay = finalPrice / numParcels
    print(f'You have to pay in x{numParcels} of R$ {totalPay:.2f} from total of R$ {finalPrice:.2f} ')
else:
    print('Invalid method.')
