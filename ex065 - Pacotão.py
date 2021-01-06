num = int(input("Digite um número:"))
soma = cont = 0
fim = False
med = 0
maior = 0
menor = 0
while not fim:
    soma += num
    cont += 1
    if cont == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor :
            menor = num
    pau = input("Deseja Continuar? [S/N]").upper().strip()
    if pau == 'S':
        num = int(input("Digite mais um número: "))
    elif pau == 'N':
        fim = True
        print("Fim da contagem")
med = soma/cont

print('A média dos números digitados foram {} sendo o maior {} e o menor {}'.format(med, maior, menor))