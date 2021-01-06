a = float(input('Digite uma medida em \033[1mmetros\033[m: '))
cm = a / 100
dam = a *10
mm = a / 1000
km = a * 1000
hm = a * 100
dm = a / 10
print('A medida {}m é equivalente a {}mm , {}dm , {}cm , {}dam , {}hm , {}km' .format(a, mm, dm, cm, dam, hm, km))

