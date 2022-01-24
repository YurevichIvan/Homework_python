import os
from pprint import pprint

def show_stat(folder_path):
    stat = {}
    for pathfile, _, files in os.walk(folder_path):
        for file in files:
            size = os.stat(os.path.join(pathfile, file)).st_size
            key = 10 ** len(str(size))
            if key in stat:
                stat[key] += 1
            else:
                stat[key] = 1
    sorted_dict = {}
    sorted_keys = sorted(sorted(stat, key=stat.get))
    for i in sorted_keys:
        sorted_dict[i] = stat[i]
    return sorted_dict




my_folder_path = r'C:\Users\Sonya\OneDrive\Рабочий стол'
pprint(show_stat(my_folder_path))
