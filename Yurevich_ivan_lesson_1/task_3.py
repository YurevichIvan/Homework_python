def transform_string(number: int) -> str:
    if number % 10 == 1 and number != 11:
        return f'{number} процент'
    elif number % 10 == 2 and  number != 12 or number % 10 == 3 and number != 13 or number % 10 == 4  and number != 14:
        return f'{number} процента'
    else:
        return f'{number} процентов'
for n in range(1, 101):  # по заданию учитываем только значения от 1 до 100
    print(transform_string(n))