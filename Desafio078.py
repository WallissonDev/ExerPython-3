num = list()
for n in range(0,5):
    num.append(int(input(f'Digite um valor para posição {n}: ')))
for p, n in enumerate(num):
    if min(num) == n:
        print(f'O menor valor é {num[p]} na posição {p}')
    if max(num) == n:
        print(f'O maior valor é {num[p]} na posição {p}')