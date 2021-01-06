
soma = int(input('Digite um número [Aperte 999 para parar]'))
nov = 999
nov = False
somaa = 0
add = 0
while  soma != 999:
    add += 1
    somaa += soma
    soma = int(input("Quer digitar mais algum número? [Aperte 999 para parar]"))

print("A soma dos números digitados é {}  ".format(somaa))


print("The end")