preço = float(input('Digite o valor do protudo: '))
print('Digite 1 para pagamento em dinheiro:')
print('Digite 2 para pagamento no cartão a vista:')
print('Digite 3 para pagamento em até 2x no cartão: ')
print('Digite 4 para pagamento em +3x (20% Juros):')
choice = int(input())
if choice == 1:
    print(f'O valor a ser pago é de R$ {preço*10/100} com 10% de desconto!')
elif choice == 2:
    print(f'O valor a ser pago é de R$ {preço*5/100} com 5% de desconto!')
elif choice == 3:
    print(f'O valor a ser pago é de R$ {preço} em 2x de R$ {preço/2:.2f}')
elif choice == 4:
    parcelas = int(input('Digite quantas parcelas: '))
    print(f'O valor a ser pago é de R$ {preço*20/100+preço}')
    print(f'O valor a ser pago por parcela é de R$ {(preço*20/100+preço)/parcelas}')
    print(f'Parcelamento acima de 2x temos juros de 20%!')
    
