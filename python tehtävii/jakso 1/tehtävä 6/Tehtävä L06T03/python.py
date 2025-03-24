def inches_to_cm(inches):
    return inches * 2.54

def format_output(inches, cm):
    return f"{inches} tuumaa on {round(cm, 2)} cm"

def main():
    while True:
        try:
            inches = float(input("Anna tuumamäärä: "))
            if inches == 0:
                print("Ohjelma lopetetaan.")
                break
            cm = inches_to_cm(inches)
            result = format_output(inches, cm)
            print(result)
        except ValueError:
            print("Syötä kelvollinen luku.")

main()