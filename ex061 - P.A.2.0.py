n = int(input("Digite um número para fazer a P.A.:"))
r = int(input("Digite a razão:"))
t = n
s = 1
while s <= 10:
    print('{} + '.format(t), end='')
    t += r
    s += 1
print('Fim')