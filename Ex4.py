#Lazaroiu Alexandru
#Exercitiul 4

numar = input("Intoduceti un numar:")
numar = float(numar)
if numar > 0:
    if numar <10:
        print("Numarul e pozitiv!")
    elif numar == 10:
        print("Numarul introdus trebuie sa fie diferit de 10!")
    else:
        print("Numarul e mai mare decat 10!")
        print("Intoduceti alt numar mai mic decat 10!")
elif numar == 0:
    print("Numarul este 0!")
else:
    numar = abs(numar)
    print(f"Numarul e pozitiv acum: {numar}!")



