'''for c in range(1, 10):
    print(c)
print("fim porra")'''
c = 1
while c < 10:
    print(c)
    c = c + 1
print('Fim,porra')

                             #QUANDO SEI O LIMITE SERVE O FOR E O WHILE,TU QUE ESCOLHE

                                                #A ORDEM DA REPETIÇÃO IMPORTA!!

r = 's'
while r == 's':                                           #VAI SERVIR PRA QUANDO FOR O ULTIMO DA FILA
    n = int(input("Digite um valor:"))
    r = str(input('Quer continuar? [S/N]:')).lower()
print("The end")

saf = 1                                                   #Contabilizar impar ou par
a = 1
par = impar = 0
while saf != 0:
    saf = int(input('Digite um número'))
    if saf % 2 == 0:
        par += 1
    else:
        impar += 1
print('Foram analisados {} números pares e {} números  impares'.format(par, impar))