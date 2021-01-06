g = str(input("Informe seu sexo: [M/F]  ")).strip().upper()[0]

while g not in 'MF':
    g = str(input("Dado invalido,digite novamente:")).strip().upper()[0]
    #print("Ta maluco,pora?? repita")

print('Registrado com sucesso,seu cisgenero')

