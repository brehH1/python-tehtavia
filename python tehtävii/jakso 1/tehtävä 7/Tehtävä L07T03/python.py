class Cat:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def miau(self):
        print("Meoooooow!")

kit = Cat("Kit", "black")
kat = Cat("Kat", "white")

print(f"{kit.name}, Color: {kit.color}")
print(f"{kat.name}, Color: {kat.color}")

kit.miau()