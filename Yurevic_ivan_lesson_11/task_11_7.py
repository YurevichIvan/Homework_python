class Complex:
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def __str__(self):
        return f'({self.number1}+{self.number2}n)'

    def __add__(self, other):
        return Complex(self.number1 + other.number1, self.number2 + other.number2)

    def __mul__(self, other):
        return Complex(self.number1 * other.number1, self.number2 * other.number2)


x = Complex(3, 3)
y = Complex(3, 3)
print('x =', x)
print('y =', y)
print('x+y =', x + y)
print('x*y =', x * y)
