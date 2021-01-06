n = 0
s = 0
cont = 0
while True:
    n = int(input("Digite um número ,se quiser parar digite 999: "))
    if n == 999:
        break
    cont += 1
    s +=  n
print(f"Foram mostrados {cont } números e a soma deles é {s}")