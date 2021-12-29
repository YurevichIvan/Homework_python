my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

def convert_list_in_str(list_in: list) -> str:
    res = []
    for i in my_list:
        if i.isalpha() == True:
            res.append(i)
        elif i.isalpha() == False and i.isdigit() == True and len(i) >= 2:
            res.append('"')
            res.append(i)
            res.append('"')
        else:
            if len(i) == 1:
                res.append('"')
                i += "0"
                i = i[::-1]
                res.append(i)
                res.append('"')
            else:
                res.append('"')
                i = list(i)
                i = '0'.join(i)
                res.append(i)
                res.append('"')
    return res
result = convert_list_in_str(my_list)
print(*result)

my_list2 = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
def convert_list_in_str2(list_in: list) -> str:
    for i in range(len(my_list2)):
        if my_list2[i].isalpha() == True:
            pass
        elif my_list2[i].isalpha() == False and my_list2[i].isdigit() == True and len(my_list2[i]) >= 2:
            my_list2[i] = f'"{my_list2[i]}"'
        else:
            if len(my_list2[i]) == 1 and my_list2[i].isdigit() == True:
                my_list2[i] = f'"0{my_list2[i]}"'
            elif len(my_list2[i]) == 1 and my_list2[i].isdigit() == False:
                pass
            else:
                my_list2[i] = f'"+0{my_list2[i][-1]}"'
    return my_list2
result = convert_list_in_str2(my_list)
print(*result)
