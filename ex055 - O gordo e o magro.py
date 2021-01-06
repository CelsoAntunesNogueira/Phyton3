gg = 0
pp = 0
for c in range(1,6):
    a = float(input('Fala teu peso aí, pessoa {}:'.format(c)))
    if c == 1:                #Fazendo isso permite que cada repetição é anotada
        gg = a
        pp = a
    else:
        if a > gg:              #Aqui é comparada qual é o mais pesado e o mais leve
            gg = a
        if a < pp:
            pp = a
print("O mais pesado foi {}".format(gg))
print("O mais leve foi {}".format(pp))

                              #OUTRA MANEIRA DE SE FAZER
lista = []
for p in range(1, 6):
    lista.append(float(input("Digite seu peso,pessoa {}:".format(p))))
print("O mais pesado é {}".format(max(lista)))
print("O mais leve é {}".format(min(lista)))
