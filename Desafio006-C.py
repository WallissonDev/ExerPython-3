
# str para valores caracters como textos, numeros
# bool para valores lógicos como true e false
# Int para número inteiros
# Float código para número com ponto, numero reais
#
##n = float(input('Digite um valor'))
##print(type(n))
# type para mostrar o tipo de numeros primitivos
#
# A baixo a maneira como eu achei pra resolver o exercício
#
#forma 1
#n = input('Digite algo')
#input('É númérico?')
#print(n.isnumeric())
#input('É maiúsculo?')
#print(n.isupper())
#
#forma 2
n = input('Digite algo')
print('Tipo de Classifiação Primitiva')
print(type(n))
print('É númérico?')
print(n.isnumeric())
print('Está em maiúsculo?')
print(n.isupper())
print('É alfanúmerico?')
print(n.isalnum())
