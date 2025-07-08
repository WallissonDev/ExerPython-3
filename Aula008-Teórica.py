# Aula sobre módulos
# Usamos o comando import para trazer funcionalidades externas ou internas
# Trazidas de bibliotcas como por exemplo a "math" já inclusa dentro do python
# import(math)
# isso trará todas as funcionalidades matemáticas como sqrt, pow, ceil, floor, trunc, factorial
# tudo da biblioteca da math
# podemos utilizar o comando from pra selecionarmos de maneira mais especificas a unica função a qual queremos
# por exemplo from math import sqrt, pow  nesse caso utilizar a vírgula para importar mais de uma da qual queremos
# o Guanabara utiliza o exemplo pra explicar modulos como quadrantes onde dentro do módulo bebida possuí café,refri, agua e etc
# usando import, pegamos todos essas bebidas
# utilizando from importamos apenas as que queremos, por exemplo
# from(bebidas)import(água)
# Forma 1 de Fazer - Import sem from para escolher a funcionalidade especifica
#
#import math
#num = int(input('Digite um Número: '))
#raiz = math.sqrt(num)
#print(f'A raiz de {num} é {math.ceil(raiz)}')
#
# Nesse caso vou arredondar utilizando o math.ceil
# Enfase em como ele foi colocado {math.ceil(raiz)} importante a biblioteca e a importação virem antes do objeto o mesmo também precisa estar em parenteses (raiz)
# posso utilizar outros comandos como o floor para arredondamento para baixo, ceil para cima, trunc para eliminar o decimal
# também posso não utilizar a biblioteca com finalidade de arrendondamento, apenas colocas :.2f para deixar apenas os 2 ultimos decimais
#
# Forma 2 - Utilizando from para especificar a funcionalidade
#
from math import sqrt, floor
num = int(input('Digite um Número: '))
raiz = sqrt(num)
print(f'A raiz de {num} é {floor(raiz)}')
# Repare que nesse caso não foi necessário adicionar o código math antes do floor, pois já especifiquei minha importanção na primeira linha adicionando sqrt e floor

