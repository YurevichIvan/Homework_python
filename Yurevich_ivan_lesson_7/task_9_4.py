class Car:
    is_police: bool = False

    def __init__(self, speed: int, color: str, name: str):
        """
        Конструктор класса
        :param speed: текущая скорость автомобиля
        :param color: цвет автомобиля
        :param name: название марки автомобиля
        """
        self._speed = float(speed)
        self._color = color
        self._name = name
        self._is_police = False



    def go(self)-> None:
        """
        Увеличивает значение скорости на 15
        :return: в stdout сообщение по формату
            'Машина <название марки машины> повысила скорость на 15: <текущая скорость машины>'
        """
        return f'Машина {self._name} повысила скорость на 15: {self._speed + 15}'


    def stop(self) -> None:
        """
        При вызове метода скорость становится равной '0'
        :return: в stdout сообщение по формату '<название марки машины>: остановилась'
        """
        return f'{self._name} остановилась'

    def turn(self, direction: str) -> None:
        """
        Принимает направление движения автомобиля
        :param direction: строковое представление направления движения, может принимать только
            следующие значения: 'направо', 'налево', 'прямо', 'назад'
        :return: в stdout сообщение по формату
            '<название марки машины>: движется <direction>'
        """
        if direction in ['направо','налево', 'прямо', 'назад']:
            return f'{self._name} движется {direction}'
        else:
            raise ValueError('нераспознанное направление движения')

    def show_speed(self) -> None:
        """
        Проверка текущей скорости автомобиля
        :return: в stdout выводит сообщение формата
            '<название марки машины>: текущая скорость <значение текущей скорости> км/час'
        """
        if self._is_police == True:
            return f'{self._name}: текущая скорость {self._speed} км/час. Вруби мигалку и забудь про скорость!'
        return f'{self._name}: текущая скорость {self._speed} км/час'

# определите классы TownCar, WorkCar, SportCar, PoliceCar согласно условия задания
class TownCar(Car):
    def show_speed(self):
        if self._speed > 60:
            return f'Alarm!!! Speed!!!'
        return f'{self._name}: текущая скорость {self._speed} км/час'

class WorkCar(Car):
    def show_speed(self):
        if self._speed > 40:
            return f'Alarm!!! Speed!!!'
        return f'{self._name}: текущая скорость {self._speed} км/час'

class SportCar(Car):
    pass

class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self._is_police = True

if __name__ == '__main__':
    town_car = TownCar(41, "red", 'WW_Golf')
    work_car = WorkCar(41, 'yellow', 'BobCat')
    police_car = PoliceCar(120, "blue", 'BMW')
    sport_car = SportCar(300, 'white', 'Ferrari')
    print(town_car.go())  # Машина WW_Golf повысила скорость на 15: 56
    print(town_car.show_speed()) # WW_Golf: текущая скорость 56 км/час
    print(work_car.show_speed())  # Alarm!!! Speed!!!
    print(town_car.stop())  # WW_Golf: остановилась
    print(police_car.show_speed())
    # BMW: текущая скорость 120 км/час
    # Вруби мигалку и забудь про скорость!
    print(sport_car.turn('назад'))  # Ferrari(SportCar): движется назад
    print(sport_car.turn('right'))



