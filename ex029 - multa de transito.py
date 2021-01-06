km = int(input('Qual foi a velocidade que você passou pelo radar??'))
if km > 80:
    print('Você ultrapassou o limite de velocidade e irá pagar uma multa!!')
    print('Sua multa é de {}'.format((km-80) * 7))
else:
    print('Ta liberado,se adianta,"menor".')
