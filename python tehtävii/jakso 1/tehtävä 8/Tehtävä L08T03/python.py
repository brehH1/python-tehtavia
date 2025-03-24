def input_grade() -> int | None:
    while True:
        grade_input = input("Syötä kurssiarvosana (0-5) tai paina Enter jättääksesi tyhjäksi: ")
        if grade_input == "":
            return None
        try:
            grade = int(grade_input)
            if 0 <= grade <= 5:
                return grade
            else:
                print("Arvosanan täytyy olla välillä 0-5. Yritä uudelleen.")
        except ValueError:
            print("Syötteen täytyy olla kokonaisluku. Yritä uudelleen.")

def collect_grades() -> list[int]:
    grades = []
    while True:
        grade = input_grade()
        if grade is None:
            break
        grades.append(grade)
    return grades

def calculate_average(grades: list[int]) -> float:
    if grades:
        return sum(grades) / len(grades)
    return 0.0

def display_results(grades: list[int]) -> None:
    average = calculate_average(grades)
    print(f"Arvosanoja yhteensä: {len(grades)}")
    print(f"Keskiarvo: {average:.1f}")

def main():
    grades = collect_grades()
    display_results(grades)

if __name__ == "__main__":
    main()