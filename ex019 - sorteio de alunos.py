import random
a = input('Quem é o primeiro aluno:')
b = input('O segundo aluno:')
c = input('O terceiro aluno:')
d = input('O ultimo aluno:')
lista = [a, b, c, d]    #Lista usamos colchetes
r = random.choice(lista)
print('O aluno escolhido foi {}'.format(r))


pó = ['Fraga', 'Zé', 'Daniel', 'Paulo', 'Celso', 'Gualberto', 'Wesley', 'Miguel']
pp = random.choice(pó)
print('Quem vai bancar o pó de galo amanhã vai ser o  {}' .format(pp))