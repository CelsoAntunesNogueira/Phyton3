a = int(input('Digite um número:'))
b = int(input('Digite o segundo número:'))
c = int(input('Digite o terceiro número'))
maior = a
if b > a and c > a:
    maior = b
if c > a and c > b:
    maior = c
menor = a
if b < a and c < a:
    menor = b
if c < a and c < b:
    menor = c
print("O maior valor foi {}".format(maior))
print('O menor valor foi {}' .format(menor))