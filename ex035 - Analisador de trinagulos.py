print( '-=' *30)
print('Analisador de triângulos')
print( '-=' *30)
a = float(input('Digite o primeiro segmento:'))
b = float(input('Digite o segundo segmento:'))
c = float(input('Digite o terceiro segmento'))
if a < b + c and b < c+ a and c < a +b:
    print('Podem se formar um trinagulo!')
else:
    print('Não podem formar um triangulo')