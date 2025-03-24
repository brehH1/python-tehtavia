class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Nimi: {self.name}, Ikä: {self.age}"

adam = Human("Adam", 18)
eva = Human("Eva", 18)

print(adam)
print(eva)