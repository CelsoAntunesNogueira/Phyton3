s = 0
co = 0
ss = 0
coo = 0
for c in range(6):
    num = int(input('Digite um número:'))
    if num % 2 ==0:
        s += num
        co += 1
    elif num % 2 !=0:
        ss += num
        coo += 1

print("Você informou {} números pares .A soma dos números é {}.". format(co, s))
print("Você informou {} números impares. A soma dos números é {}" .format(coo, ss))