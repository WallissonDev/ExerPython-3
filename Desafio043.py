peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura * altura)
if imc < 18.5:
    print(f'Abaixo do peso! {imc:.2f}')
elif imc == 18.5 or imc <= 25.0:
    print(f'Peso ideal! {imc:.2f}')
elif imc == 25.1 or imc <= 30.0:
    print(f'Sobrepeso! {imc:.2f}')
elif imc == 30.1 or imc <= 40.0:
    print(f'Obesidade! {imc:.2f}')
elif imc >= 40.1:
    print(f'Obesidade mórbida! {imc:.2f}')
