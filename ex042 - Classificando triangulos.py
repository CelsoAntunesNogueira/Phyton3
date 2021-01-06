print("Analisador de Triangulos!!!")
l1 = float(input("Digite uma medida:"))
l2 = float(input("Digite outra medida:"))
l3 = float(input("Digite o ultimo lado:"))
iso = l1 == l2 != l3 or l3 == l2 !=l1 or l2 == l1 !=l3
eqi = l1 == l2 == l3
esc = l1 != l2 != l3
if l1 + l2 > l3 or l2 + l3 > l1 or l1 + l3 >l2:
    print("Pode ser um triangulo", end=' ')
    if iso:
        print('É um isosceles!Tendo dois lados iguais')
    elif eqi:
        print("É um equilatero!Todos os lados são iguais."),
    else:
        print("É um escaleno!Todos os ângulos são diferentes")