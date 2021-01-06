nome = str(input("Digite uma frase:")).strip().upper()  #Deixou num formato só para não dar erro (espaços e deixando maisusculo)
pal = nome.split()                                      #Separou a frase em cada palavra colocando numa lista
jj = ''.join(pal)                                       #Deixou todas letras agarradas formando uma palavra só
rev = ''
for nome in range(len(jj) - 1, -1, -1):                 #Fez uma 'contagem regressiva' da palavra
    rev += jj[nome]
print('O inverso de {} é {}'.format(jj, rev))
if rev == jj:                                           #Parte de se foi ou não
    print("Temos um palíndromo")
else:
    print('A frase digitada não é um palíndromo')

                #OUTRA FORMA DE FAZER SEM O FOR

reve = jj[::-1]            #FICARIA ONDE ESTAVA O REV
print(jj, reve)