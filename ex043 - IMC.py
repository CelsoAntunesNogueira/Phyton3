print('=' * 30)
print("IMC - Descubra se você está no seu peso ideal!!")
print('=' * 30)
alt = float(input("Digite sua altura em metros:"))
pes = float(input("Digite seu peso em kg:"))
imc = pes / (alt * alt)
if imc < 18.5 :
    print("Maluco,engorda logo,se não vai morrer!!")
elif imc > 18.5 and imc < 25:
    print("Você ta no seu peso ideal")
elif imc > 25 and imc < 30:
    print("Ta gordinho veii")
else :
    print("Maluco!!Tu consegue ficar em pé??PQP emagrece ae")