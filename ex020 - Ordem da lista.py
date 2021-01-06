import random
n1 = input('Diga um nome:')
n2 = input('Diga outro nome:')
n3 = input('Ultimo nome:')
r = [n1, n2, n3]
ra = random.shuffle(r)
print(' A ordem de dar a bunda é {}'.format(r))