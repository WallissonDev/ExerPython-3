number = int(input('Digite um número: '))

colors = {
    'clean': '\033[0m',
    'red': '\033[1:31m',
    'blue': '\033[1:35m',
    'green': '\033[1:36m',
    'bolt': '\033[1m'}

print(f'Agora digite {colors['red']}1{colors['clean']} para = {colors['bolt']}Binário{colors['clean']}')
print(f'Agora digite {colors['blue']}2{colors['clean']} para = {colors['bolt']}Octal{colors['clean']}')
print(f'Agora digite {colors['green']}3{colors['clean']} para = {colors['bolt']}Hexadecimal{colors['clean']}')
choice = int(input('Digite : '))
if choice == 1:
    print(f'{number:08b}')
    print(bin(number))
# a função Bin aparentemente mostra em binário, mas não tenho certeza ainda
# Agora o número escolhido na variável number:08b converte para binário, explicação entre chaves no final
elif choice == 2:
    print(oct(number))
# utilizando a função oct(number) convertemos o inteiro para octal
elif choice == 3:
    print(hex(number))
# utilizando a função hex(number) convertemos o inteiro para hexadecimal.
#>>> '{0:08b}'.format(6)
#'00000110'
#Just to explain the parts of the formatting string:
#{} places a variable into a string
#0 takes the variable at argument position 0
#: adds formatting options for this variable (otherwise it would represent decimal 6)
#08 formats the number to eight digits zero-padded on the left
#b converts the number to its binary representation
#If you're using a version of Python 3.6 or above, you can also use f-strings: