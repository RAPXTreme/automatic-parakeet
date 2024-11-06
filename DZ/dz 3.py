name = ['тимур', 'даша', 'бегзод', 'расул', 'султан', 'азим', 'коля', 'маша']

Vibor = input('Выберите функцию Добавить/Удалить/Редактировать: ')

if Vibor == 'Добавить':
    name2 = input('Введите имя для добавления: ')
    name.append(name2)
    print(name)
elif Vibor == 'Удалить':
    name2 = input('Введите имя для удаления: ')
    name.remove(name2)
    print(name)
elif Vibor == "Редактировать":
    name2 = input('Введите имя для редактирования: ')
    if name2 in name:
        name.remove(name2)
        name3 = input('Введите новое имя: ')
        name.append(name3)
        print(name)
else:
    print('Не верный запрос!')