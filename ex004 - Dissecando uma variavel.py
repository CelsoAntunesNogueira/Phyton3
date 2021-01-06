cor = {"limpa": "\033[m",
       "red": "\033[31m",
       "azul": "\033[34m",
       "neg": "\033[1m",
       "pb" : "\033[7;30m",
       "roxo": "\033[35m",
       "ciano" : "\033[36m"}


a = input('digite \033[4malgo\033[m:')
print('O tipo primitivo desse valor é' , type(a))
print('é um numero? {}{}{}'.format(cor['ciano'], a.isnumeric(), cor['limpa']))
print('é uma letra? {}{}{}'.format(cor['pb'], a.isalpha(), cor['limpa']))
print('é uma letra ou numero?? {}{}{} ' .format(cor['red'], a.isalnum(), cor['limpa']))
print('as letras são minusculas? {}{}{}' .format(cor["neg"], a.islower(), cor['limpa']))
print('Tem algum numero decimal? {}{}{}' .format(cor["azul"], a.isdecimal(), cor['limpa']))
print('É um digito?? {}{}{}' .format(cor["roxo"], a.isdigit(), cor["limpa"]))
print('Tem letras minusculas e maisuculas?? {}{}{}' .format(cor["ciano"] , a.isupper(), cor["limpa"]))
print('Há espaços? {}{}{}'.format(cor["pb"], a.isspace() , cor["limpa"]))
print('São letras maiusculas?? {}{}{}' .format(cor["red"], a.istitle(), cor["limpa"]))





""" tipos dos is
   isspace() = se tem espaços
   istitle() = se são todas maiusculas
   isalpha() = Se tem letra
   isnumeric() = se é numero
   isalnum() = se é tem letra e numero
   islower() = se todos os caracteres estão em minuisculo
   isdecimal() = se tem apenas numero decimal 
   isdigit() = se tem algo digitado
   isupper() = se tem letras maiusculas"""


