all_products = {'Весь склад': {}}
korzina = {'Корзина': {}}

while True:
    admin = input('Что сделать? ')

    if admin.title() == 'Добавить':
        product_name = input('Введите название продукта: ')
        product_count = int(input('Введите кол-во продукта: '))
        all_products['Весь склад'][product_name] = product_count
    elif admin.title() == 'Продукты':
        print(all_products)
    elif admin.title() == 'Купить':
        product_name = input('Введите название продукта: ')
        product_count = int(input('Введите кол-во продукта: '))
        if product_name in all_products['Весь склад']:
            if all_products['Весь склад'][product_name] >= product_count:
                all_products['Весь склад'][product_name] -= product_count
                if product_name in korzina['Корзина']:
                    korzina['Корзина'][product_name] += product_count
                else:
                    korzina['Корзина'][product_name] = product_count
            else:
                print('Недостаточно товара на складе!')
        else:
            print('Товар отсутствует на складе!')
    elif admin.title() == 'Заменить':
        product_name = input('Введите товар для изменения: ')
        if product_name in korzina['Корзина']:
            new_product_name = input('Введите новый товар: ')
            new_product_count = int(input('Введите кол-во нового товара: '))
            korzina['Корзина'][new_product_name] = korzina['Корзина'].pop(product_name)
            korzina['Корзина'][new_product_name] = new_product_count
            print(korzina)
        else:
            print('Товар отсутствует в корзине!')
    elif admin.title() == 'Корзина':
        print(korzina)
    else:
        print('Неизвестная операция!')