nome = str(input('Digite seu nome:  ')).strip()
nome2 = nome.upper()
nome3 = nome.lower()
nome4 = len(nome)
nome5 = nome.split()
colors = {
    'cor1':'\033[1;33m',
    'cor2':'\033[1;34m',
    'cor3':'\033[1;35m'}
print('Seu nome maiúsculo:',colors['cor1'],nome2)
print('Seu nome minúsculo:', colors['cor2'],nome3)
print('Seu nome tem: ',colors['cor3'],nome4,'Letras')
print('Seu primeiro nome é:',colors['cor1'], nome5[0], 'E tem:', colors['cor2'],len(nome5[0]))