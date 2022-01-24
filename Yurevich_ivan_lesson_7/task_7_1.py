from os import path, mkdir

def create_starter(dir_path, dir_name, folders):
    current_path = path.join(dir_path, dir_name)
    if not path.exists(current_path):                         # проверка наличия папки
        mkdir(current_path)
    for folder in folders:
        current_folder = path.join(current_path, folder)
        if not path.exists(current_folder):
            mkdir(current_folder)


my_path = r'C:\Users\Sonya\OneDrive\Рабочий стол'
my_dir = 'my_first_project'
my_folders = ('settings', 'mainapp', 'adminapp', 'authapp')

create_starter(my_path, my_dir, my_folders)