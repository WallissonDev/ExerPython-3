# Aula 09 - Manipulando Texto
# Quando atribumos uma string a um objeto
# frase = 'Curso em vídeo python '
# Alocamos um espaço na memória para frase
# dentro disso existem mini espaços para cada letra da frase ' Curso em Video Python'
# podemos usar isso para fazer fatiamento
#frase = 'Curso em video python'
#print(frase[9])
# Mostra só a 9 posição
#frase = 'Curso em Video Python'
#print(frase[3:13])
# Mostra da posição 3 até a 13, lembrando -1 sempre no final
#frase = 'Curso em Video Python'
#print(frase[1:15:2])
# Vai de 1 até 15 pulando de 2 em
#frase = 'Curso em Video Python'
#print(frase[1::2])
# Vai pulando de 2 em 2 até o final da frase
# assim como posso tirar o 1 frase(::2) e ir pulando de 2 em 2 até o final de toda string
#
# Como escrever um texto inteiro de uma vez
# você deve escrever print e usar """ no inicio e no final do texto ijnteiro
# print(""" Texto enorme aqui """)
#
# usando o . a gente define que nosso objeto tenha uma função mesmo que ele esteja atribuido
# a uma frase já, como no exemplo
#frase = 'Curso em video Python'
#print(frase.count('o'))
# a frase executou uma função de count e mostrou quantos 'o' tem na frase atribuida a ela
# podemos utilizar multiplas funções pra localizarmos o que queremos ou alterarmos os resultados
# frase = 'Curso em Video Python'
# print(frase.upper().count('O'))
# Nesse exemplo acima transformamos a letra 'o' em maiuscula e contamos depois quantas apareceram
# frase = '   Curso em Video Python   '
# print(len(frase))
# vai me mostrar o comprimento da frase, podendo acabar com os espaços que contam como caracters utilizando o comando
#frase = '  Curso em video Python   '
#print(len(frase.strip()))
#frase = 'Curso em Video Python'
#print(frase.replace('Python','Android'))
# pra conseguir salvar essa alteração com o replace é necessário atribui-lá novamente ao objeto
# frase = frase.replace('Python','Android')
# print(frase)
# Temos também como verificar se a palavra que queremos saber está dentro do nosso objeto
#frase = 'Curso em Video Python'
#print('Curso' in frase)
#frase = 'Curso em Vídeo'
#print(frase.find('Curso'))
# vai me mostrar a posição da palavra Curso
# Lembrando que se mostrar -1 quer dizer que não existe
#frase = 'Curso em Video'
#print(frase.lower().find('video'))
# vai fazer com que a palavra video fique em minusculo e eu consiga localizar ela depois, pois em maiúsculo o V apareceria -1
#frase = ('Curso em Video Python')
#div = frase.split()
#print(div[0])
# aqui ela vai dividir a frase em uma lista transformando cada uma das palavras em uma parte da lista
# no div[0] ele vai mostrar a posição do primeiro item da lista
frase = 'Curso em Video Python'
div = frase.split()
print(div[0][2])
# Nesse exemplo ele vai dividir a frase, me mostrar a palavra da lista em posição 0 e a 2 letra dela
# 05:10 - Fatiamento de String;
# 13:50 - Análise:
#     14:15 - len();
#     14:50 - count();
#     16:35 - find();
#     18:55 - in;
# 19:35 - Transformação:
#     19:55 - replace();
#     20:50 - upper();
#     21:50 - lower();
#     22:25 - capitalize();
#     23:04 - title();
#     24:34 - strip();
#     25:08 - rtrip();
#     25:50 - lstrip();
# 26:35 - Divisão:
#     26:50 - split();
# 28:20 - Junção:
#     28:35 - join();