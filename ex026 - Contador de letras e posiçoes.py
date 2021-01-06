a = str(input('Digite uma frase:').strip())
b = a.lower()
c = b.count('a')      #contar quantos 'a' tem na frase
d = b.find('a')       #posição da primeira letra
e = b.rfind('a')
print('A letra "a" apareceu {} vezes na frase' .format(c))
print('A primeira letra "a" aparece na posição {}'.format((d)+1))
print('A ultima letra "a" aparece na posição {}'.format((e)+1))