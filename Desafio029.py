velCar = float(input('Digite a velocidade: '))
velMult = (velCar-80)*7
if velCar > 80.0:
    print(f'Você foi multado em! R$ {'\033[1;31m'}{velMult}{'\033[0m'}, pois estava andando a: {velCar}Km/h')
else:
    print(f'Muito bem, continue andando com segurança! na velocidade de {velCar}Km/h!')

# O desafio era fazer o cálculo onde, cada km/h acima de 80km/h custaria R$ 7.0
# Então fiz com que o valor que fosse acima de 80km/h fosse subtraido do mesmo e então multipliquei pelo valor da multa por km que é 7
