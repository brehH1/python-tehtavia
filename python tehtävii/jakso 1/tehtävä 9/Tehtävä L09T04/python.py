def initialize_list() -> list[str]:
    return ["apple", "banana", "cherry", "date", "elderberry"]

def get_valid_index(max_index: int) -> int:
    while True:
        try:
            index = int(input(f"Please enter an index between 0 and {max_index - 1}: "))
            if 0 <= index < max_index:
                return index
            else:
                print(f"Invalid index. Please enter a number between 0 and {max_index - 1}.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def get_valid_string() -> str:
    while True:
        user_input = input("Please enter a non-empty string: ")
        if user_input:
            return user_input
        else:
            print("Input cannot be empty. Please try again.")

def insert_string(strings: list[str], index: int, new_string: str) -> list[str]:
    strings.insert(index, new_string)
    return strings

def print_list(strings: list[str]) -> None:
    print(", ".join(strings))

def main():
    strings = initialize_list()
    print("Original list:")
    print_list(strings)
    
    max_index = len(strings)
    index = get_valid_index(max_index)
    
    new_string = get_valid_string()
    
    updated_strings = insert_string(strings, index, new_string)
    
    print("Updated list:")
    print_list(updated_strings)

if __name__ == "__main__":
    main()
