
def get_uniq_numbers(src: list):


    unique_el = set()
    tmp = set()
    for i in src:
        if i not in tmp:
            unique_el.add(i)
        else:
            unique_el.discard(i)
        tmp.add(i)
    unique_set = [el for el in src if el in unique_el]
    return unique_set



src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(*get_uniq_numbers(src))


