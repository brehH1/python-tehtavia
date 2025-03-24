pisteet = int(input("Anna pistemäärä: "))

if 0 <= pisteet <= 1:
    arvosana = 0
elif 2 <= pisteet <= 3:
    arvosana = 1
elif 4 <= pisteet <= 5:
    arvosana = 2
elif 6 <= pisteet <= 7:
    arvosana = 3
elif 8 <= pisteet <= 9:
    arvosana = 4
elif 10 <= pisteet <= 12:
    arvosana = 5
else:
    print("Pistemäärä ei ole sallittu.")
    exit()

print(f"Arvosana: {arvosana}")