def create_car(reg_number: str, brand: str, model: str, year: int) -> dict[str, dict[str, str | int]]:
    return {reg_number: {"brand": brand, "model": model, "year": year}}

def add_car(registry: dict[str, dict[str, str | int]], car: dict[str, dict[str, str | int]]) -> None:
    registry.update(car)

def create_registry() -> dict[str, dict[str, str | int]]:
    return {}

def print_by_brand(registry: dict[str, dict[str, str | int]]) -> None:
    sorted_by_brand = sorted(registry.items(), key=lambda x: x[1]["brand"])
    for reg_number, car_info in sorted_by_brand:
        print(f"{reg_number}: {car_info['brand']} {car_info['model']} ({car_info['year']})")

def print_by_reg_number(registry: dict[str, dict[str, str | int]]) -> None:
    sorted_by_reg_number = sorted(registry.items())
    for reg_number, car_info in sorted_by_reg_number:
        print(f"{reg_number}: {car_info['brand']} {car_info['model']} ({car_info['year']})")

def main():
    registry = create_registry()
    cars = [
        create_car("ABC-123", "Skoda", "Octavia", 2020),
        create_car("XYZ-789", "Toyota", "Corolla", 2019),
        create_car("DEF-456", "Volvo", "V60", 2021),
        create_car("GHI-789", "Ford", "Focus", 2018),
        create_car("JKL-012", "Honda", "Civic", 2022)
    ]
    for car in cars:
        add_car(registry, car)

    print("Autot merkin mukaan:")
    print_by_brand(registry)
    print("\nAutot rekisterinumeron mukaan:")
    print_by_reg_number(registry)

if __name__ == "__main__":
    main()