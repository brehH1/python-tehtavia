luku = int(input("Anna luku väliltä 1-10: "))

if luku < 1 or luku > 10:
    print("Virheellinen syöte!")
else:
    for i in range(1, luku + 1):
        for j in range(1, luku + 1):
            print(f"{i * j:3}", end=" ")
        print()