try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    c = a / b
except Exception as erro:
    print(f'Problema encontrado foi {erro.__class__}')
except (ValueError, TypeError):
    print(f'Tivemos um problemas com os dados que você forneceu.')
except ZeroDivisionError:
    print(f'Não podemos dividir por zero!')
except KeyboardInterrupt:
    print(f'O usuário preferiu não informar os dados')
else:
    print(f'O resultado é {c}')
finally:
    print('Volte Sempre!')