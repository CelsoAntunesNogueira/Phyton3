velho = 0
name = 0
med = 0
soma = 0
idadef = 0
for c in  range(1,5):
    print("------------- {}ª Pessoa --------------".format(c))
    nome = str(input("Qual é o seu nome?")).strip()
    idade = int(input("Qual é sua idade?"))
    sexo = str(input("Qual é o seu sexo [M/F]?")).strip().upper()
    soma += idade
    if c == 1 and sexo in 'M':
        velho = idade
        name = nome
    if sexo in'M' and idade > velho:
        velho = idade
        name = nome
    if sexo in  'F' and idade < 20:
        idadef += 1
med = soma /4
print("A media de idade do grupo é {}".format(med))
print("O cabrunco mais velho é {} e tem {} anos".format(name, velho))
print("Tem {} mulheres menores de 20 anos".format(idadef))

