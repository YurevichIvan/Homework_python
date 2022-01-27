def val_checker():
    def _val_checker(func):
       def wrapper(*args):

            if func(*args) > 0:
                return func(*args)
            else:
                raise ValueError(f'неверное значение: {args}')
       return wrapper
    return _val_checker

@val_checker()
def calc_cube(x):
    """Возведение числа в третью степень"""
    return x ** 3

if __name__ == '__main__':
    print(calc_cube(5))
    print(calc_cube('ss'))
