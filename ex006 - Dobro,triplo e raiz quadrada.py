m = int(input('Digite um número:'))
d = m * 2
t = m * 3
r = m ** (1/2)
print('O \033[4mnúmero escolhido\033[m foi \033[1m{}\033[m,o seu dobro é \033[1m{}\033[m,o seu triplo \033[1m{}\033[m e a sua raiz quadrada é \033[1m{:.2f}\033[m' .format(m, d, t, r))

          # Outra forma de fazer
print ('O número escolhido foi {} \n o seu  \033[1mdobro\033[m  é {}\n o seu \033[1mtriplo\033[m é {} \n e sua \033[1mraiz quadrada\033[m é {:.2f}' .format(m, (m*2), (m*3), (m**(1/2))))