import datetime
tom = 0
ton = 0
for c in range(1, 8):
    a = int(input('Digite o ano que a {}ª pessoa nasceu:'.format(c)))
    nas = datetime.date.today().year - a
    if nas > 18:
        tom +=1
    else:
        ton +=1
print("Tivemos {} pessoas mais velhas e {} de menor".format(tom, ton))
