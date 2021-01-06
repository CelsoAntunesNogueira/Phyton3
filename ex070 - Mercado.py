print('*' * 25)
print('  Mercadão de Madureira')
print('*' * 25)
cont = 0
menor = 0
barato = ' '
total = 0
mil = 0
while True:
    nome = str(input("Nome do produto:")).strip()
    valor = int(input("Preço:"))
    if valor > 0:
        total += valor
    if valor > 1000:
        mil += 1
        cont += 1
    if cont == 1:
        valor = menor
        barato = nome
    if valor < menor:
        menor = valor
        barato = nome
    c = " "
    while c not in 'SN':
        c = str(input('Deseja continuar? [S/N]:')).upper().strip()[0]
    if c == 'N':
        break
    print('*'*25)

print(f'Essa brincadeira deu um total de R${total} \n E os produtos que custaram mais de 1K foram {mil} \n Teu produto mais barato foi {barato}. \n Volte Sempre!! :3 ')