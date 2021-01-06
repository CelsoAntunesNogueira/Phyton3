

while True:
    n = int(input("Digite um número que você quer saber a tabuada:"))

    if n < 0:
        break
    print(f'A tabuada de {n} é :')
    for c in range (0 , 11):
        print(f'{n} * {c} = {n * c} ')


print("Programa encerrado!")