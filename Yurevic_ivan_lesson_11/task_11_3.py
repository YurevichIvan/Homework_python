class NotDigit(Exception):
    def __init__(self, txt):
        self.txt = txt

res = []
while True:
    number = input('Введите число для формирования списка (введите stop, чтоб завершить формирование списка):')
    try:
        if number == 'stop':
            break
        if number.isdigit() == False:
            raise NotDigit('Некорректный ввод! повторите ввод!')
        res.append(int(number))
    except (ValueError, NotDigit) as err:
        print(err)

print(res)