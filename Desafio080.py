ordem = list()
for i in range (1,6):
    num = int(input('Valor: '))
    ordem.append(num)
    for n, p in enumerate(ordem):
        if num < n :
            ordem.insert(p,num)
        if num > n:
            ordem.insert(p+1,num)
    print(ordem)