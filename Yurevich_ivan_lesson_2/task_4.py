my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

def convert_name_extract(list_in: list) -> list:
    list_out = []
    for i in my_list:
        name = str(i.split()[-1])
        list_out.append("Привет! {}!".format(name.capitalize()))
    return list_out
result = convert_name_extract(my_list)
print(result)


def convert_name_extract2(list_in: list) -> list:
    for i in my_list:
        list_out = []
        name2 = str(i.split()[-1]).capitalize()
        list_out = [f'Привет! {name2}!']
        return list_out
result = convert_name_extract(my_list)
print(result)