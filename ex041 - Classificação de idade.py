import datetime
id = int(input("Digite sua data de nascimento:"))
nasc = datetime.date.today().year - id
if nasc <= 9:
    print("Tu és Juvenil!")
elif nasc > 9 and nasc < 14:
    print("Tu é infantil!")
elif nasc > 14 and nasc < 19:
    print("Tú é Junior")
elif nasc > 19 and nasc < 25:
    print ("Ti é Senior")
elif nasc > 26 :
    print("Tú é MASTER!!Merece o seu pó de galo!!")
