print('='* 20)
print("Gerador de P.A")
print('='*20)
num = int(input("Digite o primeiro termo:"))
razão = int(input("Digite a razão:"))
termo = num
cont = 1
somaa = 10
total = 0
while somaa != 0:
    total += somaa           #APLICAÇÃO DA FORMULA
    while cont <= total :
        print('{} +'.format(termo), end=' ')
        termo += razão       #APLICAÇÃO DA FORMULA
        cont += 1            #CONTABILIZA O NÚMERO DE TERMOS
    print ('Pausa')
    somaa = int(input("Quer adicionar mais termos?")) #PARA ADICIONAR MAIS TERMOS E VOLTA PARA O COMEÇO
print("P.A. finalizada.Foram mostrados {} termos ".format(total))

























numb = int(input("Qual sequência do Fibonacci você deseja?"))
ff1 = 0
ff2 = 1
conta = 0

te = 3
while te <= numb:
    ff3 = ff1 + ff2
    print( '{}' .format(ff3), end=' ')
    ff1 = ff2
    ff2 = ff3
    te += 1
print('Dim')