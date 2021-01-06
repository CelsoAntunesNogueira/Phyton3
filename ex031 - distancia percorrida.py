a = float(input('Quantos km é sua viagem?'))
print('Sua viagem é de {} km' .format(a))
if a > 200:
    print('O preço de sua viagem é R${}'.format((a) * 0.45))
else:
    print('O preço de sua viagem é R${}'.format((a)* 0.50))
