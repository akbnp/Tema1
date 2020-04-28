#Lazaroiu Alexandru
#Exercitiul 3

an = input("Introduceti un an: ")
an = int(an)
while an > 0:
    if (an % 4) == 0:
        print("Anul introdus e bisect!")
        break
    else:
        print("Anul nu este bisect!")
        break
else:
    print("Introduceti un an pozitiv si diferit de 0!")
