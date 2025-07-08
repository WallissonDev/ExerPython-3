# Quando possui só IF é condição simples, IF e ELSE é condição composta e quando possuí IF, ELSE E ELIF
# Chamamos de Condição Aninhada, como a de baixo.
# Lembrando que Else não é obrigatório de ter.
# Se chama aninhada pois está uma dentro da outra, como aquelas bonecas russas.
#
nome = str(input('Qual seu nome: '))
if nome == 'Wallisson':
    print('Que nome bonito', nome)
elif nome == 'Paulo' or nome == 'Maria' or nome == 'Pedro':
    print('Um nome lendário')
elif nome in 'Ana Claudia Jéssica Juliana':
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal')
print('Tenha uma boa noite!')

