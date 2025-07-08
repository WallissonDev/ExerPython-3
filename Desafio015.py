km = float(input('Quantos Km foi rodado? '))
di = int(input('Por quantos dias foi alugado? '))
c1 = km*0.15
c2 = di*60
c3 = c1+c2
# Outra forma c1 = (km*0.15)+(di*60)
print(f'Fazendo {km} km em {di} dias o valor a se pagar é: R$ {c3:.2f} ')
