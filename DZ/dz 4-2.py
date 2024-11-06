under_liter = 0.1
over_liter = 0.25

while True:
    bottle_1 = int(input("Введите кол-во бутылок до 1л"))
    bottle_2 = int(input("Введите кол-во бутылок больше 1л"))
    overall = (bottle_1 * under_liter) + (bottle_2 * over_liter)
    print(f' Вы получаете $ {round(bottle_2)}')