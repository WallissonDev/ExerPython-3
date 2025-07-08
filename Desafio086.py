matriz = list()
zero = list()
um = list()
dois = list()
for c in range (0,9):
    valor = int(input('Digite o valor: '))
    if c <= 2:
        zero.append(valor)
    elif c >= 3 and c < 6:
        um.append(valor)
    elif c >= 6:
        dois.append(valor)
matriz.append(zero[:])
matriz.append(um[:])
matriz.append(dois[:])
print(f' {matriz[0]} ')
print(f' {matriz[1]} ')
print(f' {matriz[2]} ')