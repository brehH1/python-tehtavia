def celToFah(cel):
    return round((cel * 9/5) + 32, 1)

def fahToCel(fah):
    return round((fah - 32) * 5/9, 1)

def main():
    print(celToFah(10.0))  # 50.0
    print(fahToCel(38.0))  # 3.3

main()