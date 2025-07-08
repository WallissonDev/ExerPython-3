velCar = float(input('Digite a velocidade do carro: '))
velMul = (velCar - 80) * 7
if velCar > 80:
    print(f'Você foi multado em! R$ {velMul:.2f}!')
print('Dirija com segurança!')