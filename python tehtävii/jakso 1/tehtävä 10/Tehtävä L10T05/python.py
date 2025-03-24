import random

def generate_lottery_numbers() -> list[int]:
    return random.sample(range(1, 41), 7)

def format_lottery_numbers(numbers: list[int]) -> str:
    return " ".join(map(str, sorted(numbers)))

def save_lottery_numbers(numbers: str, file_path: str) -> None:
    try:
        with open(file_path, "a") as file:
            file.write(numbers + "\n")
    except IOError as e:
        print(f"Tiedoston kirjoittaminen epäonnistui: {e}")

def run_lottery() -> list[int]:
    numbers = generate_lottery_numbers()
    formatted_numbers = format_lottery_numbers(numbers)
    save_lottery_numbers(formatted_numbers, "lotto.txt")
    return numbers

def main():
    file_path = "lotto.txt"
    try:
        lottery_numbers = run_lottery()
        print(f"Arvotut lottonumerot: {format_lottery_numbers(lottery_numbers)}")
        print(f"Numerot on tallennettu tiedostoon {file_path}")
    except Exception as e:
        print(f"Virhe: {e}")

if __name__ == "__main__":
    main()