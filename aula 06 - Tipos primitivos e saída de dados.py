###Tipos primitivos : int , float ,bool , str
###   int = números inteiros ( 3,2,3333,9,0,-222)
###   float =  números com 'decimais' (2.4 , 9.0 , -2.555)
###   bool = valores lógicos que se usam apenas (True ou False) [as inicias tem que estar em maisuclas]
###    str = a parte de texto/ou converte numero para texto (boi,7.4, '' [string vazia])

     ####  Fazendo sem botar os tipos primtivos:

n1 = input('Digite um número: ')
n2 = input('Digite outro número:')
s = n1 + n2
print((type)(n1))
print('a soma é' , s )

      ### Fazendo corretamente !!

n1 = int(input('Digite um número:'))
n2 = int(input('Digite outro número:'))
n3 = n1 + n2
print('A soma entre {}e{} é {}' .format(n1, n2, n3))

