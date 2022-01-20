
import json
from itertools import zip_longest


def prepare_dataset(path_users_file: str, path_hobby_file: str) -> dict:
    """
    Считывает данные из файлов и возвращает словарь, где:
        ключ — ФИО, значение — данные о хобби (список строковых переменных)
    :param path_users_file: путь до файла, содержащий ФИО пользователей, разделенных запятой по строке
    :param path_hobby_file: путь до файла, содержащий хобби, разделенные запятой по строке
    :return: Dict(str: Union[List[str]|None])
    """
    users = []
    hobbies = []
    with open(path_users_file, 'r', encoding='utf-8') as usr:
        for line in usr:
            users.append(line.strip().replace(',', ' '))
    with open(path_hobby_file, 'r', encoding='utf-8') as hob:
        for line in hob:
            hobbies.append(line.strip())
    if len(hobbies) > len(users):
        exit(1)
    else:
        return {k: v for k, v in zip_longest(users, hobbies)}




dict_out = prepare_dataset('users.csv', 'hobby.csv')


with open('task_6_3_result.json', 'w', encoding='utf-8') as fw:
    json.dump(dict_out, fw, ensure_ascii=False, indent=2)
