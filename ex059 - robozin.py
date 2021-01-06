n1 = int(input("Digite um valor:"))
n2 = int(input("Digite outro valor"))
ex = 0
print('O que deseja fazer com esses valores: \n [ 1 ] Somar \n [ 2 ] Multiplicar \n [ 3 ] Qual é o maior \n [ 4 ] Novos números \n [ 5 ] Me mandar tomar no cu e ir embora'  )
print("=" * 30)
while ex != 5:
    a = int(input("Qual sua opção:"))
    if a == 1:
        nt = n1 + n2
        print('A soma de {} mais  {} é {}'.format(n1, n2, nt))
    elif a == 2:
        nx = n1 * n2
        print("A multiplicação entre {} e {} é {}".format(n1, n2, nx))
    elif a == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre os números {} e {} , o {} é maior'.format(n1, n2, maior))
    elif a == 4:
        n1 = int(input("Digite novos números:"))
        n2 = int(input("Digite outro:"))
    elif a == 5:
        print("Grosso!")
    else:
        print("Comando inválido,tente novamente")
    print('=' * 30)
    #nw = int(input('Qual comando você deseja fazer agora?'))
print("Fim")