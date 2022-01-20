from pprint import pprint


def get_parse_attrs(line: str) -> tuple:
    """Парсит строку на атрибуты и возвращает кортеж атрибутов (<remote_addr>, <request_type>, <requested_resource>)"""
    line = fr.readline().split(' ')
    return (line[0], line[5][1:], line[6]) # верните кортеж значений <remote_addr>, <request_type>, <requested_resource>


list_out = list()
with open('nginx_logs.txt', 'r', encoding='utf-8') as fr:
    for i in fr:
        line = fr.readline()
        list_out.append(get_parse_attrs(line))# передавайте данные в функцию и наполняйте список list_out кортежами

pprint(list_out)