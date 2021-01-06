

fib = int(input("Quantos termos você quer mostrar?"))
termos = 3

t1 = 0
t2 = 1

while termos <= fib:
    t3 = t1 + t2
    print('-- {}' .format(t3), end='')
    t1 = t2
    t2 = t3
    termos += 1

print('FIM')
