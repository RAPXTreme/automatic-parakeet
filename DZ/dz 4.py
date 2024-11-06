while True:
    slovo = input('Введите слово: ')
    p = slovo[::-1]
    if slovo == p:
      print("Палиндром")
    else:
      print("Не палиндром")