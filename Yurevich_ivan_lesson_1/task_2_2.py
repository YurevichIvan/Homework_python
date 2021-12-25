def sum_list_2(dataset: list) -> int:
    res = 0
    num = 0
    sum_num = 0
    for i in dataset:
        if sum_num % 7 == 0:
            res += num
        sum_num = 0
        for j in str(i):
            num = int(i)
            last_num = int(j) % 10
            sum_num += last_num
            last_num //= 10
    return res
my_list = [i ** 3 + 17 for i in range(1002) if i % 2 != 0]
result_2 = sum_list_2(my_list)
print(result_2)
