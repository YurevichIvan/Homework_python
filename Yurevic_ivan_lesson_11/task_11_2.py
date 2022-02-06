class MyZeroDivision(ZeroDivisionError):
    def __init__(self, txt):
        self.txt = txt

a = int(input('Введите частное: '))
b = int(input('Введите делитель: '))

def division(a, b):
    try:
        if b == 0:
            raise MyZeroDivision('Деление на ноль запрещено!')
    except MyZeroDivision as e:
        print(e)
    else:
        return a / b

print(division(a, b))