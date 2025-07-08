num = int(input('Digite um Número: '))
print('[ 1 ] Converter para Binário ')
print('[ 2 ] Converter para Hexadecimal ')
print('[ 3 ] Converter para Octal')
choice_number = int(input())
if choice_number == 1:
    print(f'{bin(num)[2:]}')
elif choice_number == 2:
    print(hex(num)[2:])
elif choice_number == 3:
    print(oct(num)[2:])
else:
    print('Opção Inválida! Escolha entre (1), (2), (3)!')
# Duas maneiras de fazer, com format e sem, para escolher  maneira de partição
