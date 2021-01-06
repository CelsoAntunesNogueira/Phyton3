'''                              Para colorir no terminal você usa esse comando!!

                                         \033[style;text;backm

Style :                                                           text:                           back:
0 : nenhum efeito(pode deixar até em branco)       []      30: branco     34: azul   []    40: branco       44: azul
1 : negrito                                        []      31: vermelho   35: roxo   []    41: vermelho     45: vermelho
4 : sublinhado                                     []      32: verde      36: ciano  []    42: verde        46: ciano
7 : inverte as cores com o fundo                   []      33: amarelo    37: cinza  []    43: amarelo      47: cinza

Exemplos a seguir!!'''

print('\033[1;30;41m Olá,mundo! \033[m')    #Voce coloca o codigo que quer e para tirar é só colocar "\033[m" que voltarar ao normal
print('\033[7;30m ta preto? \033[m')        #para deixar a letra da DA COR PRETA,fazer esse exemplo!!
a = int(input('Digite um número:'))
b = int(input('Digite outro numero:'))
print("Os números digitados foram \033[1;36m{}\033[m e \033[1;35m{}\033[m!!".format(a, b))   #Forma 2
nome = 'Celso'
print("Sei que só ta entrando pica,mas não desista,{}{}{}! " .format('\033[1;31m', nome, '\033[m')) #Forma 3
cores = {'limpa':'\033[m' ,
         'azul': '\033[34m',
         'vermelho':'\033[31m',
         'pb': '\033[7;30m'}
print('Você irá conseguir,{}{}{}!!!' .format(cores['azul'], nome, cores['limpa'])) #Forma 4 usando dicionario

