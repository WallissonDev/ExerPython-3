cidade = str(input('Cidade: ')).strip()
print(cidade[:5].title() == 'Santo')
# podemos usar o == para atribuir como se fosse um boolean
# então ali no print estamos falando que a string cidade, eu quero às 5 primeiros palavras
# estou falando também pra deixar em title, ou seja, primeira letra maiúscula
# logo se a primeira palavra for santo, vai ficar como Santo,
# vai pegar as 5 primeiras letras que devem ser Santo pra dar true
# no .strip eu também garanto que não tenha espaços no inicio pra confundir as 5 primeiras letras
