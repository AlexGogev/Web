class Parent:
    def __init__(self, name, age):
        self.name = name.capitalize()
        self.age = int(age)

    def __str__(self):
        return f'{self.name} is {self.age}'


class Child(Parent):
    def __init__(self, name, age, pet):
        super().__init__(name, age)
        self.pet = pet

    def __str__(self):
        return f"{super().__str__()} her pet is {self.pet}"


alison = Child("alison", 35, "mimi")

print(alison)


class new:
    def __init__(self):
        print("hello")
