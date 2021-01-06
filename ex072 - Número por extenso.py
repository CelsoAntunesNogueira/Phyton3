nu = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
      'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')

while True:
    a = int(input("Digite um número de 0 a 20:"))
    if a > -1 and a < 21:
        print(f"O número escolhido foi {(nu[a])}")
    else:
        print("Número invalido.", end=' ')
    c = ' '
    while c not in "SN":
        c = input('Deseja continuar ? [S/N]').upper().split()[0]
    if c == 'N':
        break


