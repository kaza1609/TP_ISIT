def add_to_cart(products: list, cart: list) -> None:
    """Добавление в корзину с выбором веса"""
    for k, v in enumerate(products):
        print(f"{k + 1}. {v['name']}")
    choice = int(input())
    weight = int(input('Введите число граммов: '))
    for i in cart:  # Если товар уже в корзине, вес прибавляется
        if i[0]['name'] == products[choice - 1]['name']:
            i[1] += weight
            return
    cart.append([products[choice - 1], weight])


def products_menu(products: list, cart: list) -> None:
    """Меню продуктов. С фильтрацией по калориям или простой вывод"""
    choice = input('1. Отфильтровать по числу калорий\n2. Вывести список\n')
    match choice:
        case '1':
            calories_count = int(input(f'Введите максимальное число калорий: '))
            products = list(filter(lambda x: x['calories'] <= calories_count, products))
            add_to_cart(products, cart)
        case '2':
            add_to_cart(products, cart)
        case _:
            pass


def cart_menu(cart: list) -> None:
    """Меню для корзины. С сортировкой или простой вывод"""
    choice = input('1. Отсортировать\n2. Вывести список\n')
    match choice:
        case '1':
            sort_by = input('Сортировать по (калории, белки, жиры, углеводы): ')
            match sort_by:
                case 'калории':
                    cart = sorted(cart, key=lambda x: x[0]['calories'], reverse=True)
                case 'белки':
                    cart = sorted(cart, key=lambda x: x[0]['protein'], reverse=True)
                case 'жиры':
                    cart = sorted(cart, key=lambda x: x[0]['fats'], reverse=True)
                case 'углеводы':
                    cart = sorted(cart, key=lambda x: x[0]['carbohydrates'], reverse=True)
                case _:
                    pass
        case '2':
            pass
        case _:
            pass
    print_cart(cart)
    calculate_props(cart)


def calculate_props(cart: list) -> None:
    """Подсчет суммарных характеристик продуктов в корзине"""
    sum_calories, sum_protein, sum_fats, sum_carbohydrates = 0, 0, 0, 0
    for i in range(len(cart)):
        sum_calories += cart[i][0]['calories'] * (cart[i][1] / 100)
        sum_protein += cart[i][0]['protein'] * (cart[i][1] / 100)
        sum_fats += cart[i][0]['fats'] * (cart[i][1] / 100)
        sum_carbohydrates += cart[i][0]['carbohydrates'] * (cart[i][1] / 100)
    print(f'Суммарная калорийность: {sum_calories} ккал.\nБелки: {sum_protein} г.\n'
          f'Жиры: {sum_fats} г.\nУглеводы: {sum_carbohydrates} г.')


def print_cart(cart: list) -> None:
    """Вывод корзины {НАЗВАНИЕ} {МАССА}"""
    for i in cart:
        print(f'{i[0]["name"]} {i[1]} г.')
