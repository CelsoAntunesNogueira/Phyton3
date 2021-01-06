from math import factorial
n = (int(input("Digite um número para fatorial: ")))
h = factorial(n)
print('O fatorial de {} é {}'.format(n, h))




                        #OUTRA FORMA DE FAZER


num = int(input("Escolha um número para fazer o fatorial:"))
c = num
f = 1
while c > 0:
    print('{}' .format(c), end= '')
    print(' x ' if c > 1 else ' = ', end= '' )
    f *= c
    c -= 1
print("O fatorial de {} é {}".format(num, f))