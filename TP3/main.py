from classes import *


if __name__ == '__main__':
    cars = [
        PassengerCar('Т721АР', 'Toyota 1', 'Economy'),
        PassengerCar('М912ВФ', 'Mercedes 1', 'Business'),
        PassengerCar('К453МС', 'Renault 1', 'Comfort'),
        Truck('Н900ЖВ', 'Daewoo 1', True),
        Truck('Ш512ФК', 'Toyota 2', False)
    ]
    taxi_company = TaxiCompany('Test company', cars)

    passengers = [
        Passenger('test1', 'test-mobile1', Luggage(10, '10*10')),
        Passenger('test2', 'test-mobile2', Luggage(70, '10*10'))
        # Passenger('test3', 'test-mobile3', Luggage(10, '10*10')),
        # Passenger('test4', 'test-mobile4', Luggage(10, '10*10'))
    ]
    taxi_company.call(100, passengers)
    print('Все машины:', list(map(lambda x: f'{x.taxi_model} {x.taxi_number} {x.taxi_type}', cars)))
