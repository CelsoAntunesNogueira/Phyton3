#SÓ ADICIONAR 'BREAK' NO ULTIMO 'IF' OU NO FINAL MESMO
#NA DUVIDA DOS CONTADORES E SOMADORES ,ASSISTA AULA 15 NA PARTE PRATICA

n = 0
s = 0
while True:         #PARA FAZER UMA REPETIÇÃO INFINITA É FAZER ISSO,ADICIONAR "TRUE"
    n = int(input("Digite um número:"))
    if n == 999:
        break
    s += n
print(f"A soma vale {s}")     #NOVA FORMA DE UTILIZAR O PRINT

