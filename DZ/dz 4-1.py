while True:
    numeric = int(input('Введите число: '))

    for i in range(1, 11):
        print(numeric, '*', i, '=', numeric * i)