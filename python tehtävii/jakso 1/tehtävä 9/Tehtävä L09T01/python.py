def create_list() -> list[int]:
    return [1, 2, 3, 4]

def modify_element(numbers: list[int], index: int, new_value: int) -> bool:
    try:
        numbers[index] = new_value
        return True
    except IndexError:
        return False

def safe_print_element(numbers: list[int], index: int) -> None:
    try:
        print(numbers[index])
    except IndexError:
        print("Virheellinen indeksi")

def main():
    numbers = create_list()
    print(f"Alkuperäinen lista: {numbers}")

    if modify_element(numbers, 2, 100):
        print(f"Muokattu lista: {numbers}")
    else:
        print("Elementin muokkaus epäonnistui.")

    if modify_element(numbers, 5, 500):
        print(f"Muokattu lista: {numbers}")
    else:
        print("Elementin muokkaus epäonnistui.")

    safe_print_element(numbers, 1)
    safe_print_element(numbers, 10)

if __name__ == "__main__":
    main()