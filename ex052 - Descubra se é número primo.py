print("Detector de números primos!!")
a = int(input('Digite o número que você quer saber se é primo ou não:'))
p = 0
for c in range(1, a+1):
    if a % c ==0:
        print('\033[31m', end=' ')
        p += 1
    else:
        print('\033[33m', end=' ')
    print(c, end= ' ')
print("\n\033[mO número {} foi divido {} vezes".format(a, p ))
if p ==2:
    print("\033[1;32mÉ um número primo!!")
else:
    print('\033[1;32mNão é um número primo!')