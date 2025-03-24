def get_number_input() -> str:
    user_input = input("Syötä luku (tai tyhjä, jos haluat lopettaa): ")
    return user_input

def classify_number(input_str: str) -> str:
    if input_str == "":
        return "empty"
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

    while True:
        user_input = get_number_input()
        classification = classify_number(user_input)

        if classification == "empty":
            break
        elif classification == "int":
            write_to_file(user_input, "kokonaisluvut.txt")
            int_count += 1
        elif classification == "float":
            write_to_file(user_input, "liukuluvut.txt")
            float_count += 1
        else:
            print("Virheellinen syöte! Syötä luku tai jätä kenttä tyhjäksi.")

    return int_count, float_count

def main():
    int_file = "kokonaisluvut.txt"
    float_file = "liukuluvut.txt"
    int_count, float_count = process_numbers()
    print(f"Tallennettu {int_count} kokonaislukua tiedostoon {int_file}")
    print(f"Tallennettu {float_count} liukulukua tiedostoon {float_file}")
    print("Tarkista tiedostojen sisältö tekstieditorilla.")

if __name__ == "__main__":
    main()
