nome = str(input('Qual nome da sua cidade: ')).strip()
n1 = nome.title()
nome1 = n1.split()
nome2 = nome1[0:1]
nome3 = 'Santo' in nome2
print('Possui Santo no Inicio: ','\033[0;33m', nome3,'\033[0m')