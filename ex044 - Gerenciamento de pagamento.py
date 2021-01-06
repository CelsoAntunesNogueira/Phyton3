pag = float(input("Informe seu pagamento:R$"))
print("""Escolha a forma de pagamento:
[ 1 ] Dinheiro
[ 2 ] Cartão
[ 3 ] Cheque""")
op = int(input(print("Qual a forma de pagamento:")))
dedin = pag * 10 / 100
parc = pag * 5 / 100
parc3 = pag * 20 / 100
if op == 1 or op == 3:
    print("Seu pagamento terá um desconto de R${},logo terá que pagar R${} ".format(dedin, pag - dedin))
elif op == 2:
    print("""Será a vista ou parcelado?
    [ 1 ] A vista
    [ 2 ] Parcelado em 2 vezes
    [ 3 ] Parcelado em 3 vezes""")
    cart = int(input("Escolha a forma de pagamento:"))
    if cart == 1:
        print("Seu pagamento terá desconto de R${}, logo terá que pagar R${}".format(parc, pag - parc))
    elif cart == 2:
        print("Você pagará no preço normal, R${}".format(pag))
    elif cart == 3:
        print("Você irá pagar com um acrescimo de {},logo terá que pagar R${}" .format(parc3, pag + parc3))
    else:
        print("\033[31mOpção Inválida,tente novamente")
else:
    print("\033[31mOpção inválida,tente novamente")
