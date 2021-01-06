soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma = soma + c  #Pode usar += tbm serve vou colocar abaixo
        cont +=  + 1
print('A soma dos multiplos impares de 3 é \033[31m{}\033[m e a soma deles são \033[31m{}\033[m'.format(cont, soma))
