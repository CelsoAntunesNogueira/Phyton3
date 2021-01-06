a = input("Qual a cidade que você nasceu??").strip()
b = 'Santo' in a                                             #Gambiarra
c = 'santo' in a                                             #   //
print(a[:5].upper() == 'SANTO')                              #Jeito certo
print(b, c)