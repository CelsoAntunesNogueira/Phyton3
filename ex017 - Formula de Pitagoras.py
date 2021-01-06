from math import hypot
 #FORMA 1
o = float(input('Digite o cateto oposto:'))
a = float(input('Digite o cateto adjacente'))
h = hypot(o, a)
print("A hipotenusa é {}".format(h))





 #FORMA 2
co = float(input('Digite o cateto oposto:'))
ca = float(input('Digite o cateto adjacente:'))
hip = (ca**2 + co**2) ** (1/2)
print('com as somas do catetos {} e {} sua hipotenusa é {:.2f}' .format(co, ca, hip))