print("=" * 20 )
print("     CADASTRO!!")
print('=' * 20)
p18 = 0      #Pessoas +18
h = 0        #quantidade de macho
m19 = 0       #Mulher novinha
f = 0
while True:
    id = int(input("Idade :"))
    if id > 18:
        p18 += 1
    gen = " "
    while gen not in 'MF':
        gen = str(input('Sexo [M/F]:')).upper().split()[0]
    if gen == "M":
        h += 1
    if gen == 'F' and id <20:
        m19 += 1
    c = " "
    while c not in 'SN':
        c = str(input('Quer continuar [S/N]:')).upper().split()[0]
    if c == 'N':
        break
    print("=" * 10)
print(f'Nesse cadastro ,foi contado  \n {p18} pessoas maiores de idade \n {h} homens \n {m19} mulheres menores de idade. ')