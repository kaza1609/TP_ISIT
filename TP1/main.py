import math


def first_task():
    distance = float(input('Введите расстояние (м): '))
    duration = float(input('Введите время в пути (мин): '))
    gender = input('Введите пол (М/Ж): ')

    avg_speed = round((distance / duration) * 60 / 1000, 2)
    match gender:
        case 'М':
            steps_count = math.ceil(0.8 * distance)
        case 'Ж':
            steps_count = math.ceil(0.5 * distance)
        case _:
            print('Пол введен неверно.')
            return

    if avg_speed < 4:
        result = 'Побольше ходи!!!'
    elif 4 <= avg_speed < 6:
        result = 'Продолжай в том же духе!'
    else:
        result = 'А ты герой!'

    print(f'Средняя скорость движения: {avg_speed} км/ч\nЧисло шагов: {steps_count}\nСостояние здоровья: {result}')


def second_task():
    height = float(input('Введите высоту стен (м): '))
    length_first = float(input('Введите длину первой пары стен (м): '))
    length_second = float(input('Введите длину второй пары стен (м): '))
    repair_type = input('Введите вид ремонта (обои или краска): ')

    wall_square = 2 * height * (length_first + length_second)

    match repair_type:
        case 'обои':
            wallpaper_price = float(input('Введите стоимость рулона обоев: '))
            wallpaper_width = float(input('Введите ширину рулона обоев: '))
            wallpaper_length = float(input('Введите длину рулона обоев: '))

            wallpaper_square = wallpaper_length * wallpaper_width
            wallpaper_amount = math.ceil(wall_square / wallpaper_square)
            wallpaper_sum = wallpaper_amount * wallpaper_price

            print(f'Количество рулонов обоев: {wallpaper_amount}\nСтоимость ремонта: {wallpaper_sum}\n'
                  f'Площадь комнаты: {wall_square}')
        case 'краска':
            paint_price = float(input('Введите стоимость 1 литра краски: '))
            paint_consumption = float(input('Введите расход краски на 1 кв.м.: '))

            paint_amount = math.ceil(wall_square * paint_consumption)
            paint_sum = paint_amount * paint_price

            print(f'Литров краски: {paint_amount}\nСтоимость ремонта: {paint_sum}\nПлощадь комнаты: {wall_square}')
        case _:
            print('Тип ремонта введен неверно.')


if __name__ == '__main__':
    while True:
        # first_task()
        second_task()
