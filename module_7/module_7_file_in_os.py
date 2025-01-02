import os
import time

print('Текущая рабочая директория:', os.getcwd())

files = [f for f in os.listdir() if os.path.isfile(f)]
print('\nФайлы в директории:', files)

print(f'Директории в директории:{[d for d in os.listdir() if os.path.isdir(d)]}\n')

print(f'\nРазмер файла "{files[0]}": {os.stat(files[0]).st_size} байт')
print(f'Абсолютный путь к файлу "{files[0]}": {os.path.abspath(files[0])}')

for root, dirs, files in os.walk('.'):
    for file in files:
        filepath = os.path.join(root, file)
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(filepath)
        parent_dir = os.path.dirname(filepath)
        abs_path = os.path.dirname(os.path.abspath(filepath))
        print(f'\nОбнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, '
              f'Время изменения: {formatted_time}, Родительская директория: {parent_dir}, '
              f'Абсолютный путь:{abs_path}')
