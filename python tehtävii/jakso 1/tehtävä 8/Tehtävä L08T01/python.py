def input_registration_number():
    registration_number = input("Syötä rekisterinumero (tai paina Enter jättääksesi tyhjäksi): ")
    return registration_number if registration_number else None

def collect_registration_numbers():
    registration_numbers = []
    while True:
        number = input_registration_number()
        if number is None:
            break
        registration_numbers.append(number)
    return registration_numbers

def sort_registration_numbers(numbers):
    return sorted(numbers)

def display_sorted_numbers(numbers):
    for number in numbers:
        print(number)

def main():
    numbers = collect_registration_numbers()
    sorted_numbers = sort_registration_numbers(numbers)
    display_sorted_numbers(sorted_numbers)

if __name__ == "__main__":
    main()