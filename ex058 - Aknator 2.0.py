import random

#tu = int(input("Digite um número de 1 a 10 ,vamos ver se tu advinha o que pensei:"))
ak = random.randint(1, 10)
acertou = False
palp = 0
while not acertou:
    tu = int(input("Digite um número ae se você consegue acertar"))
    if tu == ak:
        acertou = True
        print("Acertou mizeravi,foi o número {} , você precisou de {} tentativas".format(ak, palp))
    else :
        if tu > ak:
            print('Passou,chutou muito alto,tenta denovo')
            palp += 1
        elif tu < ak:
            print('Mais  .. machista')
            palp += 1


