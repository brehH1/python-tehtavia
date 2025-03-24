def get_student_names():
    names = []
    while True:
        name = input("Enter student name: ")
        if name == "":
            break
        names.append(name)
    return ",".join(names)

def count_students(names):
    return len(names.split(","))

def main():
    names = get_student_names()
    student_count = count_students(names)
    print(f"Student count: {student_count}")
    print(names)

main()