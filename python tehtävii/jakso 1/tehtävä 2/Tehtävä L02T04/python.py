from datetime import datetime

etunimi = input("Anna etunimesi: ")
syntymavuosi = int(input("Syntymävuotesi: "))

nykyvuosi = datetime.now().year

ika = nykyvuosi - syntymavuosi

print(f"Hei {etunimi}, olet {ika} vuotta.")
