#TUPLAS SÃO VARIAVEIS COMPOSTAS
#AS TUPLAS SÃO IMUTÁVEIS!!
#TUPLAS UTILAZAM PARENTESES () OU SEM NADA


lanche = ("Hambúrguer" , 'Suco', 'Pizza', 'Pudim')
print(lanche[1])                  #USANDO O ESQUEMA DE FATIAMENTO DA AULA 09
print(lanche[-1])                 #PEGA O ULTIMO ,QUE NO CASO O PUDIM
print(lanche[1:3])             #LEMBRANDO O QUE O ULTIMO (O Nº3) NÃO É CONTADO,SÓ O ANTECESSOR DELE
print(lanche[2:])               #VAI DE PIZZA ATÉ PUDIM
print(lanche[-3:])              #COMEÇA NO SUCO (NÚMEROS NEGATIVOS PODEM SER USADOS COMO CONTAR DE TRAS PARA FRENTE

print(sorted(lanche))     #COLOCA EM ORDEM ALFABETICA SUA TUPLA


for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!')

                            #OUTRA FORMA DE FAZER ESSE BGL DO FOR
for cont in range(0,len(lanche)):
    print(F"Eu vou comer {lanche[cont]}")
    print(cont)               #SE EU QUISER SABER A QUANTIDADE DE ITENS
print('Comi pra caramba!')

                            #OUTRA FORMA DE FAZER TBM DE POSIÇÃO
for pos, comida in enumerate(lanche):                             #Enumarete enumera os itens
    print(f"Eu vou comer {comida} na posição {pos}")


a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a          #EM TUPLAS NESSE PIQUE,VOCÊ VAI JUNTAR OS ITENS,BOTANDO A 2ª TUPLA LOGO APÓS A 1ª TUPLA TERMINAR
print(c)
print(c.count(5))   #VAI CONTAR QUANTOS 5 TEM NA TUPLA
print(c.index(4))   #MOSTRA A POSIÇÃO DO NÚMERO NA TUPLA
print(c.count(9))   #QUANDO NÃO TEM O ITEM NA TUPLA,ELE BOTA 0
print(c.index(5))   #MOSTRA A POSIÇÃO DO NÚMERO,SE CASO TIVER OUTRO IGUAL FAZER ISSO ABAIXO PQ ELE SÓ PEGA O PRIMEIRO
print(c.index(5, 1)) #SE EU QUISER PEGAR O PROXIMO NÚMERO REPETIDO,VAI SER CONTADO À PARTIR DA POSIÇÃO 1


                   #VOCÊ PODE COLOCAR VARIOS DADOS DISTINTOS NA TUPLA
pessoa = ("Celso", 22, "M", 70)
print(pessoa)
del(pessoa)   #FORMA DE 'APAGAR' A TUPLA,MAS É ELA POR COMPLETO
print(pessoa)
