from random import randint
from time import sleep
#d =('role o dado:'))
d20 = randint(1, 20)
print('\033[1;31m O dado foi jogado..\033[m')
sleep(2)
if d20 == 20:
    print("\033[7;30mDano crítico!!!!\033[m")
print( 'Deu o número' , d20)
