player1 = input("Игрок 1, выберите камень, ножницы или бумага: ")
player2 = input("Игрок 2, выберите камень, ножницы или бумага: ")

if player1 == player2:
    print("Ничья!")
elif (player1 == "камень" and player2 == "ножницы") or \
     (player1 == "ножницы" and player2 == "бумага") or \
     (player1 == "бумага" and player2 == "камень"):
    print("Игрок 1 победил!")
else:
    print("Игрок 2 победил!")
