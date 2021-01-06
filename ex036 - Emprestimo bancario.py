import  time
casa = float(input("Olá!Qual é o \033[31mvalor\033[m da casa que você quer \033[31mcomprar\033[m? "))
sal = float(input("\033[32mQuanto você ganha?"))
pcl = int(input("\033[33mVai financiar em quantos anos??\033[m"))
fin = casa/(pcl*12)
min = sal * 30 / 100
print("\033[1mPara pagar o financiamento de {} meses de uma casa de R${:.2f}, com um salário de {:.2f}".format(pcl, casa, sal))
print("ciente que o valor da parcela não pode passar de 30% do seu sálario,ou seja..\033[m ")
time.sleep(3)
if fin <= sal:
    print("Seu emprestimo foi \033[1;35mACEITO!!\033[m")
else:
    print("Seu emprestimo foi \033[1;36mNEGADO!!\033[m")