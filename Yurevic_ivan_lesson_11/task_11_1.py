import datetime
class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def converter(cls, date: str):
        day, month, year = map(int, date.split('-'))
        if cls.data_valid(day, month, year):
            return f'число: {day}, месяц: {month}, год: {year}'
        raise ValueError

    @staticmethod
    def data_valid(day, month, year):
        true_date = True
        if (month == 2 and day > 28) or (month == 4 or month == 6 or month == 9 or month == 11 and day > 30) or day > 31:
            print('Некорректный день')
            true_date = False
        if month < 1 or month > 12:
            print('Некорректный месяц')
            true_date = False
        if len(str(year)) > 4 or year > int(datetime.datetime.today().strftime("%Y")):
            print('Некорректный год')
            true_date = False
        return true_date


if __name__ == '__main__':
    try:
        my_date = Date.converter('02-02-2021')
        print(my_date)
    except (ValueError) as err:
        print(err)
