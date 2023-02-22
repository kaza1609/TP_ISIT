from abc import ABC, abstractmethod
from functools import reduce


class Luggage:

    def __init__(self, weight: int, size: str):  # Size str т.к. нужно рассчитывать каждую сторону, а не площадь
        self.weight = weight
        self.size = size

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, w):
        if w < 0:
            raise ValueError('Negative weight')
        self.__weight = w

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, s):
        if s == '':
            raise ValueError('Size is empty')
        self.__size = s

    def __str__(self):
        return f'Weight: {self.weight} Size: {self.size}'


class Passenger:

    def __init__(self, name: str, mobile: str, luggage: Luggage):
        self.name = name
        self.mobile = mobile
        self.luggage = luggage

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, n):
        if n == '':
            raise ValueError('Name is empty')
        self.__name = n

    @property
    def mobile(self):
        return self.__mobile

    @mobile.setter
    def mobile(self, m):
        if m == '':
            raise ValueError('Mobile is empty')
        self.__mobile = m

    def __str__(self):
        return f'Name: {self.name}\nMobile: {self.mobile}\nLuggage: {self.luggage}'


class Taxi(ABC):

    def __init__(self, taxi_number: str, taxi_model: str):
        self.taxi_number = taxi_number
        self.taxi_model = taxi_model

    @property
    def taxi_number(self):
        return self.__taxi_number

    @taxi_number.setter
    def taxi_number(self, tn):
        if tn == '':
            raise ValueError('Taxi number is empty')
        self.__taxi_number = tn

    @property
    def taxi_model(self):
        return self.__taxi_model

    @taxi_model.setter
    def taxi_model(self, tm):
        if tm == '':
            raise ValueError('Taxi model is empty')
        self.__taxi_model = tm

    @abstractmethod
    def compute_cost(self, distance: int, passengers: list) -> tuple | None:
        pass


class PassengerCar(Taxi):
    taxi_type = 'Легковое такси'

    def __init__(self, taxi_number: str, taxi_model: str, taxi_class: str):
        super().__init__(taxi_number, taxi_model)
        self.taxi_class = taxi_class

    @property
    def taxi_class(self):
        return self.__taxi_class

    @taxi_class.setter
    def taxi_class(self, tc):
        if tc not in ["Economy", "Comfort", "Business"]:
            raise ValueError('Taxi class is not exists')
        elif tc == '':
            raise ValueError('Taxi class is empty')
        self.__taxi_class = tc

    def compute_cost(self, distance: int, passengers: list) -> tuple | None:
        if len(passengers) > 4:
            return None
        sum_weight, x_size, y_size = 0, 0, 0
        for i in passengers:
            sum_weight += i.luggage.weight
            spl = i.luggage.size.split('*')
            x_size += int(spl[0])
            y_size += int(spl[1])
        if sum_weight > 50 or x_size > 40 or y_size > 50:
            return None
        taxi_cls = {
            "Economy": 1,
            "Comfort": 3,
            "Business": 5
        }
        return self, taxi_cls[self.taxi_class] * (distance + sum_weight)

    def __str__(self):
        return f'Taxi number: {self.taxi_number}\nTaxi model: {self.taxi_model}\nTaxi class: {self.taxi_class}'


class Truck(Taxi):
    taxi_type = 'Грузовое такси'

    def __init__(self, taxi_number: str, taxi_model: str, is_loader: bool):
        super().__init__(taxi_number, taxi_model)
        self.is_loader = is_loader

    def compute_cost(self, distance: int, passengers: list) -> tuple | None:
        if len(passengers) > 2:
            return None
        sum_weight = 0
        for i in passengers:
            sum_weight += i.luggage.weight
        return self, 150 + 3 * distance + (int(self.is_loader) * sum_weight)

    def __str__(self):
        return f'Taxi number: {self.taxi_number}\nTaxi model: {self.taxi_model}\nLoader: {self.is_loader}'


class TaxiCompany:

    def __init__(self, name: str, cars: [PassengerCar | Truck]):
        self.name = name
        self.cars = cars

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, n):
        if n == '':
            raise ValueError('Name is empty')
        self.__name = n

    @property
    def cars(self):
        return self.__cars

    @cars.setter
    def cars(self, c):
        if len(c) == 0:
            raise ValueError('Cars is empty')
        self.__cars = c

    def call(self, distance: int, passengers: list[Passenger]) -> None:
        available_cars = [x.compute_cost(distance, passengers) for x in self.cars if
                          x.compute_cost(distance, passengers) is not None]
        if not available_cars:
            print('Доступных машин нет.')
            return

        print('Доступные машины:', list(map(lambda x: f'{x[0].taxi_model} {x[0].taxi_number} '
                                                      f'{x[1]} руб. {x[0].taxi_type}', available_cars)))
        selected_car = reduce(lambda x, y: x if x[1] < y[1] else y, available_cars)
        print(f'Водитель в пути. Номер машины: {selected_car[0].taxi_number} '
              f'Стоимость поездки: {selected_car[1]} руб. '
              f'Тип транспорта: {selected_car[0].taxi_type}')
        self.cars.remove(selected_car[0])

    def __str__(self):
        return f'Name: {self.name}\nCars: {[x.taxi_model for x in self.cars]}'
