nota1 = float(input("Digite sua primeria nota:"))
nota2 = float(input("Digite sua segunda nota:"))
media = (nota1+ nota2)/2
print("Sua media foi {}!" .format(media))
if media >= 7.0:
    print("Parabéns você passou!")
elif media < 5.0:
    print("Você está reprovado!")
elif media > 5.1 and media < 6.9:
    print("Está em recuperação!!")
    