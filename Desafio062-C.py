pa = int(input('Digite o primeiro termo : '))
ra = int(input('Digite a razão: '))
termos = 10
dez = pa + ra * termos
pa_fixa = pa
i = 0
proximo = 0
while termos != 0:
    for i in range (pa_fixa, pa_fixa+(termos*ra), ra):
        print(i)
        pa_fixa += ra
    termos = int(input('Digite novo termo: '))


