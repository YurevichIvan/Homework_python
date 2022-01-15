num = 14
generator = (num for num in range(1, num + 1) if num % 2 != 0)
for num in generator:
    print(num)