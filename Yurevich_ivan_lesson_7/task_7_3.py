import os
import shutil

root_dir = r'C:\Users\Sonya\PycharmProjects\pythonProject\my_project'
s_file = 'index.html'
for root, dirs, files in os.walk(root_dir):
    if s_file in files:
        templates_path = os.path.join(root_dir, 'templates')
        if not os.path.exists(templates_path):
            os.mkdir(templates_path)
        name_dir = os.path.split(root)[1]
        copy_path = os.path.join(templates_path, name_dir)
        if not os.path.exists(copy_path):
            os.mkdir(copy_path)
        for file in files:
            if not os.path.exists(os.path.join(copy_path, file)):
                shutil.copy2(os.path.join(root, file), copy_path)