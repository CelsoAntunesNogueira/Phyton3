a = float(input('Quantos dias o carro foi alugado??'))
b = float(input('Rodou quantos km??'))
c = a * 60
d = b * 0.15

print('Sua despeza é de R${}\n dos dias foram R${} \n e da kilometragem foi R${} '.format((c+d), a, b))