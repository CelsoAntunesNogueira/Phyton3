num = int(input("Digite um número inteiro:"))
print("""Escolha para qual conversão você quer: 
[ 1 ] para Binário
[ 2 ] para Octal
[ 3 ] para Hexadecimal""")
opç = int(input("Sua opção é:"))
if opç == 1:
    print("A conversão de {} para Binario é {}" .format(num, bin(num)[2:]))
elif opç == 2:
    print("A conversão de {} para Octal é {}" .format(num, oct(num)[2:]))
elif opç == 3:
    print("A conversão de {} para Hexadecimal é {}" .format(num, hex(num)[2:]))
else:
    print("Digito errado,tente novamente.")


