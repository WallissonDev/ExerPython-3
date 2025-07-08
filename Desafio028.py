from random import randint
comp = int(input('Digite o número que estou pensando: '))
pc = randint(0, 5)
if comp == pc:
    print(f'Parabens! pensei em! {pc}')
else:
    print(f'Infelizmento errou pensei em! {pc}!')

# Minha lógica aqui foi a seguinte:
# Importei a biblioteca random pra utilizar o método radint
# Então fiz com que minha variável/objeto recebesse essa função pensando num número de 0 a 5
# associei um novo objeto com input, para receber o número do usuário
# depois fiz com que se o número que o usuário digitou fosse igual ao que o computador gerou com random
# escrevesse parabéns, caso contrário, um infelizmente
# usei isso com o True fazendo assim comp == pc