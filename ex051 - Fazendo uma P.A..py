print('=' * 15)
print('10 TERMOS DE UMA P.A.')
print('=' * 15)
a = int(input("Digite o primeiro termo:"))
r = int(input("Digite a razão:"))
d = a + 10 *r
s = 0
ca = 0
for c in range(a, d, r):

    print(' {} '.format(c), end=' ')
