import time
a = int(input("Escolha um número para começar a contagem regressiva:"))
for c in range(a, -1, -1 ):
    time.sleep(1)
    print(c)