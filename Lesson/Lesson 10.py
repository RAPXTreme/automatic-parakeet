# class Animal:
#     def make_sound(self, s):
#         print(s)
#
# class Horse(Animal):
#     pass
#
# pony = Horse()
# pony.make_sound("Igogo")
from curses.textpad import rectangle
from symtable import Class

# class Begzod:
#     def make_jizn(self, a):
#         print(a)
#
# class Azamat(Begzod):
#         pass
#
# Begzod = Azamat()
# Begzod.make_jizn("Казах")

# class Car:
#     def __init__(self, model, color, year):
#         self.model = model
#         self.color = color
#         self.year = year
#
# class SuperCar(Car):
#     def __init__(self, model, color, year, sponsor):
#         super().__init__(model, color, year)
#         self.sponsor = sponsor

# class Calculate:
#     @classmethod
#     def summary(cls, a, b):
#         return a + b
#
# print(Calculate.summary(2, 4))

# class Recrangle:
#     def __init__(self, width, heught):
#         self.width = width
#         self.heught = heught
#
#     @property
#     def area(self):
#         return self.width * self.heught
#
# rectangle = Recrangle(4,5)
# print(rectangle.area)
#
# rectangle.width = 6
# print(rectangle.area)

# class Worker:
#     def __init__(self, name, position):
#         self.name = name
#         self.position = position
#
# class HR(Worker):
#     def __init__(self, name, position):
#         super().__init__(name, position)
#
#     def show_position(self, worker):
#         print(worker.name, worker.position)
#
# jordan = Worker('Jordan', 'Junior')


class Player:
    def __int__(self, power, speed, accuracy, stamina):
        self.power = power
        self.speed = speed
        self.accuracy = accuracy
        self.stamina = stamina

class GaolKeeoer(Player):
    def __init__(self, power, speed, accuracy, stamina):
        super().__init__(power, speed, accuracy, stamina)

    def save(self):
        print("Поймал мяч")
