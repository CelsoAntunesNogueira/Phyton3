import datetime
nasc = int((input("Digite o ano do seu nascimento:")))
nas = datetime.date.today().year - nasc
if nas == 18:
    print("Está na hora de se alistar,vem capinar!!!")
elif nas < 18:
    falt = 18 - nas
    print("Você ainda não está na idade de se alistar!Resta {} anos.".format(falt))
else:
    passou = nas - 18
    print("Passou da idade,{} anos após!!,vai pagar multa e mamar o sargento".format(passou))