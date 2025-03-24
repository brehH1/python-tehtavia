def read_names_from_file(file_path: str) -> list[str]:
    try:
        with open(file_path, "r") as file:
            names = file.readlines()
            return [name.strip() for name in names]
    except FileNotFoundError:
        raise FileNotFoundError(f"Tiedostoa {file_path} ei löytynyt.")
    except IOError as e:
        raise IOError(f"Tiedoston käsittelyssä tapahtui virhe: {e}")

def count_names(names: list[str]) -> int:
    return len(names)

def count_name_occurrences(names: list[str]) -> dict[str, int]:
    name_occurrences = {}
    for name in names:
        name_occurrences[name] = name_occurrences.get(name, 0) + 1
    return name_occurrences

def print_name_statistics(total_count: int, name_occurrences: dict[str, int]) -> None:
    print(f"Nimien kokonaismäärä: {total_count}")
    for name, count in name_occurrences.items():
        print(f"{name}: {count}")

def main():
    file_path = "nimet.txt"
    try:
        names = read_names_from_file(file_path)
        total_count = count_names(names)
        name_occurrences = count_name_occurrences(names)
        print_name_statistics(total_count, name_occurrences)
    except Exception as e:
        print(f"Virhe: {e}")

if __name__ == "__main__":
    main()