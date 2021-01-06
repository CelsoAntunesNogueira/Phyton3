from datetime import date
a = int(input('Digite um ano e falarei se é um ano bissexto ou não!E para analisar o ano atual digite 0:'))
if a ==0:
    a = date.today().year
if a % 4 == 0 and a %100 != 0 or a % 400 == 0:
    print('esse ano é bissexto!!')
else:
    print('Não é um ano bissexto!')

