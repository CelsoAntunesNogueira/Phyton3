import random
ak = random.randint(0, 10)
c = 0
print(f'Bora jogar Par o Impar ,sua putinha')
while True:
    n = int(input('Digite um valor: '))

    t = ak + n
    reslut = (n + ak ) % 2
    pi = ' '
    while pi not in 'PI':
        pi = str(input("Par ou Impar [P/I]: ")).strip().upper()[0]
    if pi == 'P':
        if t % 2 ==0 :
            print('Você venceu!')
            c +=1
        else:
            print('Você perdeu')
            break
    elif pi == "I":
        if t % 2 != 0:
            print("Você venceu!")
            c += 1
        else:
            print('Tu perdeste!')
            break



print(f' Game Over,putinha! Você ganhou {c} vezes')


