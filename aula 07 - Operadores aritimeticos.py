'''                  Operadores Aritimeticos

   + : Adição                ** : Potência  (o comando 'pow' tbm serve)
   - : Subtração              % : Resto da divisão
   * : Multiplicação         // : Divisão inteira
   / : Divisão               == : Igual (tem que usar os dois mesmo.)
   **(1/2) : Para fazer raiz quadrada


                      Ordem de Precedência

   1º : O que estiver entre parenteses ()
   2º : Potencia **
   3º : Multiplicação,Divisão,Resto da divisão ou Divisão inteira (o que aparecer primeiro faz)
   4º : Soma e Subtração
   '''
a = int(input('Digite um valor:'))
b = int(input('Outro valor:'))
s = a + b
su = a - b
m = a * b
d = a / b
p = a ** b
r = a % b
di = a // b

print('A soma é {}, a subtração é {}, a multiplicação é {} ' .format(s, su, m) , end=' ' ) #Esse ", end=' '" é pra deixar os print abaixo na mesma linha,deixe um espaço nas aspas para não deixar agarrado?#
print((', a divisão é {:.1f}' .format(d)))  #Esse ':.1f' é o numero que quero que seja mostrado depois da virgula#
print('a potencia é {:=^4},o resto da divisão é {} e divisão inteira é {}' .format(p, r, di))

