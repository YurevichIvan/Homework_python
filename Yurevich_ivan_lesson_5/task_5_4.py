from time import perf_counter

def get_numbers(src: list):


    result = [src[i] for i in range(1, len(src)) if src [i] > src [i-1]]
    return result

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(*get_numbers(src))

#Подумайте, как можно сделать оптимизацию кода по памяти, по скорости.

start = perf_counter()
result2 = (src[i] for i in range(1, len(src)) if src [i] > src [i-1])
print(*result2)
print(perf_counter() - start)