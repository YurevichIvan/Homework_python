def thesaurus(*args) -> dict:

    dict_out = {}  # результирующий словарь значений
    for i in args:
        if i[0] in dict_out:
            dict_out[i[0]] += [i]
        dict_out.setdefault(i[0], [i])

    return dict_out


print(thesaurus("Иван", "Мария", "Петр", "Илья", "Марк", "Парт"))