# x = lambda e: e*4
#
# side = int(input('Введите сторону квадрата: '))
# print(x(side))
from email.charset import add_alias
from fileinput import close
from random import choice

# def spam2(a, b, c=8):
#     print(a+b+c)
#
# spam2(3,5, 10)

# def spam1(*args):
#     return args
#
# print(spam1(1,2,3,4,5,6))

# def spammer(*args):
#     for a in args:
#         print(a)
#
# spammer(1,2,3,4,5,6,7)

# def spam1(**kwargs):
#     for k,v in kwargs.items():
#         print(k,v)
#
# spam1(name='ma1',age=23)

clients = {}
opened_rooms = [i for i in range(1,21)]
closed_rooms = []

def add_client(name, room):
    clients[name] = room
    opened_rooms.remove(room)
    closed_rooms.append(room)

def del_client(name):
    opened_rooms.append(clients[name])
    closed_rooms.remove(clients[name])
    clients.pop(name)

def show_rooms():
    return closed_rooms

while True:
    choice = input('Что хотите сделать? :')
    if choice.lower() == 'добавить':
        client_name = input('Введите имя: ')
        print(opened_rooms)
        client_room = int(input('Введите номер для клиента: ' ))
        if client_room in opened_rooms:
            add_alias(client_name, client_room)
            print('Успешно добавлено!')
        else:
            print('Похоже номер занят')
    elif choice.lower() == 'удалить':
        client_name = input('Введите имя для удаления: ')
        if client_name in clients:
            del_client(client_name)
            print('Успешно удалено')
        else:
            print('Похоже, что-то пошло не так')
    elif choice.lower() == 'номер':
        print(show_rooms())
    else:
        print('Неизвестная операция')
