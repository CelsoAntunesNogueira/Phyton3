num = int(input('Digite um número de 0 a 9999:'))
unidade = num // 1 % 10
dezena = num // 10 % 10
cent= num // 100 % 10
milhar = num //1000

#A ideia é fazer o numero ficar com decimal e depois pegar esse decimal para classificar como unidade,dezena,centena ou milhar

print(unidade)
print(dezena)
print(cent)
print(milhar)