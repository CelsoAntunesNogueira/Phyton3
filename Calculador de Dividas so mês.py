print('=' * 30)
print('{:^30}'.format('Calculador de Dividas:'))
print('='* 30)

soma = 0


while True:
    divida = str(input('Digite uma das suas dividas:'))
    valor = float(input('Quanto é sua divida: '))
    soma += valor
    fim =str(input("Desja continuar? [S/N]:")).strip().upper()[0]
    if fim == 'N':
        break
fe = float(input("Quanto você tem no  fundo de emergencia?? "))

print(f"O total do mês é  R$ 1045,00 e seu gasto foi de R${soma} \n e vai sobrar {1045 - soma}")
print(f'resta {10000 - fe} reais para chegar alcançar no seu fundo de emergencia')