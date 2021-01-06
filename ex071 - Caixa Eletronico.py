print('-' * 30)
print('{:^30}'.format('Banco Priuzao'))
print('-' *30)

saque = int(input("Quanto você deseja sacar??"))
mont= saque                                           #Valor para ser descontado
contced = 0                                           #contador de cedulas
ced = 50                                              #começa a subtrair pelo maior
while True:
    if mont >= ced:                                 #Se meu total for maior que a maior nota eu subtraio ate
        mont -= ced                                 # for um número menor que a cedula maior quie no caso 50
        contced += 1                                #e vou contando quantas notas foram e dps passo para as notas menores
    else:
        if contced > 0:
            print(f'total de {contced} notas de R$ {ced}')   #Contagem das notas
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        contced = 0
        if mont == 0:
            break
print("Obrigado por Utilizar o nosso banco,pau no seu cu")





















'''while True:
    saque = int(input('Quanto deseja sacar?'))
    cinq = saque // 50                           #SABER QUANTAS NOTAS
    if cinq != 0:                                 #SE CASO NÃO TIVER COMO PEGAR MAIS NOTA DE 50
        resto = saque - 50                         #AÍ DIMINUI O SAQUE MENOS 50
        vinte = resto // 20                        #SABER QUANTAS NOTAS DE 20 DÁ
                                   #SE DER PARA PEGAR TD DE 50 SEM SOBRAR NADA ,ENCERRA

    if vinte !=0:                                  #SE Ñ TIVER COMO MAIS PEGAR NOTA DE 20

        restoII = resto - 20                         # OUTRA SUBTRAÇÃO
        dez = restoII // 10                        #FAZENDO POR NOTA DE 10


    if dez != 0:                                    #SE Ñ TIVER COMO MAIS PEGAR EM NOTA DE 10
        restoIII = restoII - 10                       #SUBTRAÇÃO
        um = restoIII // 1

    if um != 0:
        restIV = um

    else:
        break

print (f'Dos {saque} \n foram {cinq} notas de 50 \n {vinte} notas de 20 \n {dez} notas de 10 \n {um} notas de 1')'''






















#while True:
   # sacar = int(input("Quanto deseja sacar:"))
