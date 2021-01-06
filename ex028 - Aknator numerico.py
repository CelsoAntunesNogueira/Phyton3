import random
from  time import sleep
num = int(input('Digite um número de 1 a 5 que irei tentar advinhar:'))
a = random.randint(0, 5)
print('Pensando ..')
sleep(2)
print("O número foi {}".format(num))
print('E pensei no número {}'.format(a))
if num == a :
    print("Eu acertei! ")
else:
    print('Você ganhou!!')
