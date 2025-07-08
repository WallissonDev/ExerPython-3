num = list()
while True:
   b = int(input('Digite um valor: '))
   if b not in num:
       num.append(b)
       print('Valor adicionado com Sucesso!')
   else:
       print('Valor repetido, não vou adicionar!')
   c = str(input('Quer continuar? [S:N]: '))
   if c in 'Nn':
       break
print(num)  