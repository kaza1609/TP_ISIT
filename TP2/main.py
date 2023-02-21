import goods
import funcs
import json

if __name__ == '__main__':
    cart = []
    while True:
        choice = input("1. Категория молочного\n2. Категория сладкого\n"
                       "3. Категория овощей\n4. Категория фруктов\n5. Категория мяса\n6. Корзина\n7. Завершить\n")
        match choice:
            case '1':
                products = [goods.MILK, goods.CHEESE, goods.YOGURT, goods.KEFIR, goods.CREAM]
                funcs.products_menu(products, cart)
            case '2':
                products = [goods.SWEET, goods.CHOCOLATE, goods.COOKIE, goods.CAKE, goods.CUPCAKE]
                funcs.products_menu(products, cart)
            case '3':
                products = [goods.CARROT, goods.CUCUMBER, goods.TOMATO, goods.POTATO, goods.PEPPER]
                funcs.products_menu(products, cart)
            case '4':
                products = [goods.APPLE, goods.ORANGE, goods.PEAR, goods.BANANA, goods.LEMON]
                funcs.products_menu(products, cart)
            case '5':
                products = [goods.BEEF, goods.BACON, goods.SAUSAGE, goods.PORK, goods.MUTTON]
                funcs.products_menu(products, cart)
            case '6':
                funcs.cart_menu(cart)
            case '7':
                choice = input('1. Сохранить и завершить\n2. Вывести информацию о прошлых приемах пищи\n')
                match choice:
                    case '1':
                        with open('data.json', 'w', encoding='UTF-8') as outfile:
                            json.dump(cart, outfile, ensure_ascii=False, indent=4)
                        break
                    case '2':
                        data = json.load(open('data.json', encoding='UTF-8'))
                        funcs.print_cart(data)
                    case _:
                        pass
