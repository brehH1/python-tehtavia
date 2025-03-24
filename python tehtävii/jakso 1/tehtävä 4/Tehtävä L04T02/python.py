lukuja = 0
summa = 0

while True:
    syote = input("Anna luku: ")
    if syote == "":
        break
    luku = int(syote)
    lukuja += 1
    summa += luku

print("Lukuja annettu:", lukuja)
print("Lukujen summa:", summa)