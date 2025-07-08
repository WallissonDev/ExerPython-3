from math import pow
weight = float(input('Whats you current Weight? KG: '))
size = float(input('Whats your size? M: '))
size_Cube = pow(size,2)
imc = weight / size_Cube
if imc < 18.5:
    print(f'You light weight. {imc:.2f}')
elif imc == 18.5 or imc < 25.0:
    print(f'You perfect weight. {imc:.2f}')
elif imc == 25.0 or imc < 30.0:
    print(f'Youre overweighted. {imc:.2f} ')
elif imc == 30.0 or imc < 40.0:
    print(f'Youre obese. {imc:.2f}' )
else:
    print(f'Youre in morbidal weight {imc:.2f}')
