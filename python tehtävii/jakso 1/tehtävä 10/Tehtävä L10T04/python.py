def get_number_input() -> str:
    user_input = input("Syötä luku: ")
    return user_input.strip()

def classify_number(input_str: str) -> str:
    if input_str == "":
        return "error"
    try:
        int(input_str)
        return "int"
    except ValueError:
        try:
            float(input_str)
            return "float"
        except ValueError:
            return "error"

def write_to_file(number: str, file_path: str) -> None:
    try:
        with open(file_path, "a") as file:
            file.write(number + "\n")
    except IOError as e:
        print(f"Tiedoston kirjoittaminen epäonnistui: {e}")

def process_numbers() -> tuple[int, int]:
    int_count = 0
    float_count = 0
    int_file = "kokonaisluvut.txt"
    float_file = "liukuluvut.txt"
    
    while True:
        input_str = get_number_input()
        classification = classify_number(input_str)
        
        if classification == "int":
            write_to_file(input_str, int_file)
            int_count += 1
        elif classification == "float":
            write_to_file(input_str, float_file)
            float_count += 1
        else:
            print("Virheellinen syöte. Ohjelma päättyy.")
            break
    
    return int_count, float_count

def main():
    int_count, float_count = process_numbers()
    print(f"Tallennettu {int_count} kokonaislukua tiedostoon kokonaisluvut.txt")
    print(f"Tallennettu {float_count} liukulukua tiedostoon liukuluvut.txt")
    print("Tarkista tiedostojen sisältö tekstieditorilla.")

if __name__ == "__main__":
    main()
