soma = c = 0
while True:
    num = int(input('Digite um valor : '))
    if num == 999:
        break
    soma += num
    c += 1
print(f'O valor da soma é {soma}')
print(f'A quantia de números inteiros foi {c}')