cor = {"neg": "\033[1m",
       "red": "\033[31m" ,
       "azul" : "\033[34m" ,
       "pb": "\033[7;30m",
       "limpa": "\033[m"}

a = int(input('Digite um número : '))
an = a - 1
su = a + 1
print ('O número que você escolheu foi {}{}{} !! Seu sucessor é {}{}{} e o seu antecessor é {}{}{}'.format(cor["pb"], a, cor["limpa"],cor["red"], su, cor["limpa"],cor["neg"] , an, cor["limpa"]))

          # Você pode fazer desse jeito também
print('O número que você escolheu foi \033[4m {}\033[m!! Seu sucessor é o \033[4m{}\033[m e o seu antecessor é \033[4m{}\033[m' .format(a, (a+1), (a-1)))