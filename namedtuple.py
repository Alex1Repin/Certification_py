#Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК.
#Соберите информацию о содержимом в виде объектов namedtuple.
#Каждый объект хранит:
#* имя файла без расширения или название каталога,
#* расширение, если это файл,
#* флаг каталога,
#* название родительского каталога.
#В процессе сбора сохраните данные в текстовый файл используя логирование.


import os
import sys
import logging
from collections import namedtuple

logging.basicConfig(filename='log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

def process_directory(path):
    try:
        items = os.listdir(path)
        for item in items:
            item_path = os.path.join(path, item)
            if os.path.isdir(item_path):
                directory_name = os.path.basename(item_path)
                log_message = f"Found directory: {directory_name}"
                logging.info(log_message)
                Directory = namedtuple('Directory', ['name', 'extension', 'is_directory', 'parent_directory'])
                directory = Directory(name=directory_name, extension='', is_directory=True, parent_directory=path)
                print(directory)
                process_directory(item_path)
            else:
                file_name, file_extension = os.path.splitext(item_path)
                file_name_without_extension = os.path.basename(file_name)
                log_message = f"Found file: {file_name_without_extension}"
                logging.info(log_message)
                File = namedtuple('File', ['name', 'extension', 'is_directory', 'parent_directory'])
                file = File(name=file_name_without_extension, extension=file_extension, is_directory=False, parent_directory=path)
                print(file)
    except FileNotFoundError:
        log_message = f"Directory not found: {path}"
        logging.error(log_message)
        print(log_message)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        directory_path = sys.argv[1]
        process_directory(directory_path)
    else:
        print("Please provide the directory path as command line argument.")