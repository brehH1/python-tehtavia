summa = 0

for i in range(1, 6):
    luku = float(input(f"Anna {i}.luku: "))
    
    if luku > 0:
        summa += luku

print(f"Lukujen summa on: {summa}")


