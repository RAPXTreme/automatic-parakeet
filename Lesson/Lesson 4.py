name = ["Бегзод", "Бегзод 1", "Бегзод 2","Бегзод 3"]
telefon = ["+79379992", "+79379993", "+79379994","+79379995"]
usluga = ["чай", "кофе", "кола","сок"]

while True:
    vvod = input("Что вы хотите сделать?: ")

    if vvod == "номер":
        telefon2 =input('Введите имя')
        telefon.append(telefon2)
        print(telefon)
    elif vvod == "имя":
        name2 =input('Введите номер ')
        name.append(name2)
        print(name)
    elif vvod == "услуга":
        usluga2 =input('Введите услугу ')
        usluga.append(usluga2)
        print(usluga)
    else:
        print('Неврная команда')


