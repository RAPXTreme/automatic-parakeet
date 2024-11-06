# class Animal:
#     def make_sound(self):
#         pass
#
# class Dog(Animal):
#     def make_sound(self):
#         return "Гав-гав"
#
# class Cat(Animal):
#     def make_sound(self):
#         return "Мяу-мяу"
#
# class Cow(Animal):
#     def make_sound(self):
#         return "Мууу"
#
# dog = Dog()
# print(dog.make_sound())

class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def display_info(self):
        return f"Марка: {self.brand}, Год выпуска: {self.year}"

class Car(Vehicle):
    def __init__(self, brand, year, num_doors):
        super().__init__(brand, year)
        self.num_doors = num_doors

    def display_info(self):
        return f"{super().display_info()}, Количество дверей: {self.num_doors}"

class Motorcycle(Vehicle):
    def __init__(self, brand, year, type_motorcycle):
        super().__init__(brand, year)
        self.type_motorcycle = type_motorcycle

    def display_info(self):
        return f"{super().display_info()}, Тип мотоцикла: {self.type_motorcycle}"

car = Car("Toyota", 2020, 4)
motorcycle = Motorcycle("Harley-Davidson", 2018, "Cruiser")

print(car.display_info())
print(motorcycle.display_info())
