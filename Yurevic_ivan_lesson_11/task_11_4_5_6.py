class Warehouse:


    def __init__(self):
        self._dict = {}

    def get_equip(self, equipment):

        self._dict.setdefault(equipment.group_name(), []).append(equipment)

    def extract(self, name):

        if self._dict[name]:
            self._dict.setdefault(name).pop(0)


class Equipment:


    def __init__(self, name, make, year):
        self.name = name
        self.make = make
        if year == int(year):
            self.year = year
        else:
            raise TypeError('Неверный тип года')
        self.group = self.__class__.__name__

    def group_name(self):
        return f'{self.group}'

    def __repr__(self):
        return f' (Наименование: {self.name}, номер: {self.make}, дата изготовления: {self.year})'


class Printer(Equipment):


    def __init__(self, series, name, make, year):
        super().__init__(name, make, year)
        self.series = series

    def action(self):
        return 'Печать документа'


class Scaner(Equipment):


    def __init__(self, name, make, year):
        super().__init__(name, make, year)

    def action(self):
        return 'Сканирование документа'


class Xerox(Equipment):


    def __init__(self, name, make, year):
        super().__init__(name, make, year)

    def action(self):
        return 'Копирование документа'

if __name__ == '__main__':
    try:
        warehouse = Warehouse()

        scaner = Scaner('HP', '111', 1990)
        warehouse.get_equip(scaner)
        print(scaner.action())

        scaner = Scaner('Xerox', '222', 2020)
        warehouse.get_equip(scaner)

        scaner = Scaner('HP', '333', 2022)
        warehouse.get_equip(scaner)

        xerox = Xerox('Xerox', '444', 1888)
        warehouse.get_equip(xerox)
        print(xerox.action())

        printer = Printer('Sony', '333', 126, 2018)
        warehouse.get_equip(printer)
        print(printer.action())


        print(warehouse._dict)

        warehouse.extract('Scaner')
        print()
        print(warehouse._dict)
    except ValueError as err:
        print(err)
