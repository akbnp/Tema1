# Lazaroiu Alexandru
# Exercitiul 5

alegere = """1 - Afisare lista de cumparaturi
2 – Adaugare element
3 – Stergere element
4 – Sterere lista de cumparaturi
5 - Cautare in lista de cumparaturi
"""
alegere = input(alegere)
if alegere == "1":
    print("Afisare lista de cumparaturi")
elif alegere == "2":
    print("Adugare element")
elif alegere == "3":
    print("Stergere element")
elif alegere == "4":
    print("Sterere lista de cumparaturi")
elif alegere == "5":
    print("Cautare in lista de cumparaturi")
else:
    print("Alegerea nu exista. Reincercati")

# #varianta 2 - nu iese din program pana nu se introduce o optiune din meniu
# alegere = """1 - Afisare lista de cumparaturi
# 2 – Adaugare element
# 3 – Stergere element
# 4 – Sterere lista de cumparaturi
# 5 - Cautare in lista de cumparaturi
# """
# while True:
#     alegere = input(alegere)
#     if alegere == "1":
#         print("Afisare lista de cumparaturi")
#         break
#     elif alegere == "2":
#         print("Adaugare element")
#         break
#     elif alegere == "3":
#         print("Stergere element")
#         break
#     elif alegere == "4":
#         print("Sterere lista de cumparaturi")
#         break
#     elif alegere == "5":
#         print("Cautare in lista de cumparaturi")
#         break
#     else:
#         print("Alegerea nu exista. Reincercati")

