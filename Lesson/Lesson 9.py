# class Comment:
#     def __init__(self, username, text, likes=0):
#         self.username = username
#         self.text = text
#         self.likes = likes
#
# Comment1 = Comment("Бегзод", 'Black', 203)
#
# print(Comment1.username)
# print(Comment1.text)
# print(Comment1.likes)

# class Car:
#     def __init__(self, model, color, year):
#         self.model = model
#         self.color = color
#         self.year = year
#
#     def change_colar(self, new_colar):
#         self.color = new_colar
#
#     def stop(self):
#         print("Машина остановись")
#
# gentra = Car('Ravon', 'Black', 2022)
#
# gentra.change_colar('White')
# print(gentra.color)

# class Bank:
#     def __init__(self, client, balans=0):
#         self.client = client
#         self.balans = balans
#
#     def deposit(self, amount):
#         self.balans += amount
#
#     def cash(self, amount):
#         self.balans -= amount
#
#     def my_balance(self):

class User:
    def __init__(self, name, email, age, telefon):
        self.name = name
        self.email = email
        self.age = age
        self.telefon = telefon

    def change_name(self, new_name):
        self.name = new_name

    def change_name(self, new_email):
        self.email = new_email

    def change_name(self, new_age):
        self.age = new_age

    def change_name(self, new_telefon):
        self.telefon = new_telefon

