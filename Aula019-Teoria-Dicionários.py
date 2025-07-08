# listas = list() / []
# tuplas = tuple() / ()
#pessoas = {'Nome' : 'Wallisson', 'Sexo' : 'M', 'Idade' : 25}
#print(pessoas['nome'])
#print(pessoas['idade'])
#print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.') # IMPORTANTE! notar que usamos aspas duplas pra poder acessar o indice, pois já está dentro de um format string ''
#print(pessoas.keys()) # nome, sexo, idade
#print(pessoas.values()) # wallisson, M, 25
#print(pessoas.items()) # mostra tudo, nome,wallisson,sexo,m,idade,25
#for k in pessoas.keys():
    #print(k) # vai mostrar nome, sexo, idade
#for k in pessoas.values():
    #print(k) # vai mostrar Wallisson, M, 25
#del pessoas['sexo'] # Podemos usar para apagar o elemento/identificador
#pessoas['nome'] = 'Leandro' ---- Podemos usar isso para alterar o elemento que foi atribuido anteriormente a nome
#pessoas['peso'] = 98.5 ---- Podemos também adicionar novos elementos futuramente
#for k, v in pessoas.items():
    #print(f'{k} = {v}') # Como näo temos o enumerate, usamos o items
# o K é meu indentificador = nome,sexo,idade e o V meu elemento = Wallisson,M,25
#
# TOPICO 2
#
#brasil = list()
#estado1 = {'uf' : 'Rio de Janeiro' , 'sigla' : 'RJ' }
#estado2 = {'uf' : 'Säo Paulo', 'sigla' : 'SP' }
#brasil.append(estado1)
#brasil.append(estado2)
#print(brasil) # Uma lista composta, possuindo os dois dicionários separadamente, podendo ser acessado por indice
# esse indice vai ser acessado por um valor integro em uma lista [0] = estado1 sendo o dicionário o elemento 0 da lista
# e para acessar o elemento dentro do dicionário utilizamos um valor de identificador, por exemplo, uf ou sigla
#print(brasil[0]['uf']) # -> Rio De Janeairo
#print(brasil[1]['sigla']) # -> SP
#
# TOPICO 3
#
estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy()) # Náo podemos fazer fatiamento em elementos de um dicionário, pra isso usamos .copy()
for e in brasil:
    #print(e) # Vai mostrar todo o dicionário, no caso o identificador e o elemento
    #for k, v in e.items():
        #print(f'O campo {k} tem valor {v}.') # vai analisar todo o dicionário
    for v in e.values():
        print(v, end = '  ')
    print()
# from random import randint
# from time import sleep
# from operator import itemgetter
# ordem = list()
# jogo = { 'jogador1' : randint(1,6),
#          'jogador2' : randint(1,6),
#          'jogador3' : randint(1,6),
#          'jogador4' : randint(1,6)}
# ranking = dict()
# print('Valores Sorteados:')
# for k, v in jogo.items():
#     print(f'O {k} tirou = {v}')
# ranking = sorted(jogo.items(), key = itemgetter(1), reverse = True)
#
#sum(partidas) comando que soma os valores dentro de uma lista