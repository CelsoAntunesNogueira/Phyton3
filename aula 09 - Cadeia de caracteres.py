                                                 #FATIAMENTO

frase = 'Curso em video Python'
f = frase[3]             #Para mostrar o caractere que eu quero                     (lembrando que se começa contando do 0)
g = frase[2:3]           #Para mostrar o caractere que eu quero até certo caractere (lembrando que no final é um caractere antes)
h = frase[4:19:2]        #Vai mostrar os caracteres de 2 em 2 dentro do limite que coloquei de caracteres
i = frase[:3]            #Quando faço isso,irei mostrar do começo até onde limitei -1 .Sem precisar colocar o 0 antes dos :
j = frase[5:]            #Deixando o meio vazio significa que vai até o final da frase
k = frase[3::6]          #Mesma coisa que o de cima,mas mostrando de 6 em 6

print(f)
print(g)
print(h)
print(i)
print(j)
print(k)

                                                   #ANALISES DE STRING

len(frase)              #Mostra a quantidade de caracteres e seus espaços
frase.count('o')        #Mostra a quantidade do caracterer que escolhi,que no caso o 'o'
frase.count('o' , 0, 12)#Mesma coisa que acima,só que limitado
frase.find('d')         #Indica onde o caractere começa na frase
'Curso' in frase        #Pergunta se tem a palavra que eu quero na frase


                                                #TRANSFORMAÇÃO DE STRING

frase.replace('Curso', 'Android') #Troca a primeira string pela segunda
frase.upper()                     #Deixa o que ta minusculo para Maiusculo
frase.lower()                     #Faz o contrario que digitei acima
frase.capitalize()                #Deixa a inicial da em maiusculo e o restante da frase minusculo
frase.title()                     #Todo começo de palvra fica maiuscula
frase.strip()                     #Deixa de contar os espaços vazios no começo e no final da frase
frase.rstrip()                    #mesma coisa do de cima,só que o final
frase.lstrip()                    #mesma coisa só que esquerda
frase.split()                     #ele divide string em cada palavra ,convertendo uma frase em um lista
'-'.join(frase)                   #Converte os espaços em branco entre palavras em traços

