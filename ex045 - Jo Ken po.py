import  random
import time
adv =("tesoura", "papel", "pedra")
pc = random.randint(0, 2)
print("Ei,Viado!Vamos jogar Jokenpo!")
tu = int(input("""Digite o que for jogar na mão:
[ 0 ] Tesoura
[ 1 ] Papel
[ 2 ] Pedra"""))
print("Jo")
time.sleep(1)
print("Ken")
time.sleep(1)
print("Po!")
print('=/'*30)
print("O computador escolheu {}".format(adv[pc]))
print("Você escolheu {}".format(adv[tu]))
print('=/' *30)
if pc == 0:   #JOGOU TESOURA
    if tu ==0 :
        print("Empate lesbico!!")
    elif tu == 1:
        print("Você perdeu!")
    elif tu == 2:
        print("Você ganhou!")
    else:
        print('JOGADA INVALIDA,SABE CONTAR NÃO FDP?')
if pc == 1:       #JOGOU PAPEL
    if tu == 0:
        print('Você ganhou!')
    elif tu == 1:
        print("Empate!!")
    elif tu == 2:
        print('Você perdeu!')
    else:
        print('JOGADA INVALIDA,ESCREVE DIREITO ARROMBADO!')
if pc == 2:        #JOGOU PEDRA
    if tu == 0:
        print("Você perdeu!")
    elif tu == 1 :
        print('Você ganhou!')
    elif tu == 2:
        print("Empate!!")
    else:
        print("JOGADA INVALIDA,TENTA DNV VIADO")


