import os
import string

def list_directories(path='.'):
    return [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]

def list_files(path='.'):
    return [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

def list_all(path='.'):
    return os.listdir(path)

path = r'C:\Users\Роллан\work\Labs'
print("Директории:", list_directories(path))
print("Файлы:", list_files(path))
print("Всё содержимое:", list_all(path))

#2
def check_access(path):
    print("Существует:", os.path.exists(path))
    print("Читаемый:", os.access(path, os.R_OK))
    print("Записываемый:", os.access(path, os.W_OK))
    print("Исполняемый:", os.access(path, os.X_OK))

check_access(path)

#3
def path_info(path):
    if os.path.exists(path):
        print("Путь существует")
        print("Имя файла:", os.path.basename(path))
        print("Директория:", os.path.dirname(path))
    else:
        print("Путь не существует")
path = r"C:\Users\Роллан\work\Labs\Lab6\Buildinfunctions.py"
path_info(path)
#4
def count_lines(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return sum(1 for _ in file)

filename = 'text.txt'
print("Количество строк:", count_lines(filename))
#5
def write_list_to_file(filename, lst):
    with open(filename, 'w', encoding='utf-8') as file:
        file.writelines(f"{item}\n" for item in lst)

data = ['Jojo', 'Gurenn lagan', 'onepiece']
write_list_to_file('text.txt', data)

#6
for letter in string.ascii_uppercase:
    with open(f"{letter}.txt", 'w', encoding='utf-8') as file:
        file.write(f"Файл {letter}.txt создан\n")
#7
def copy_file(source, destination):
    with open(source, 'r', encoding='utf-8') as src, open(destination, 'w', encoding='utf-8') as dst:
        dst.write(src.read())

copy_file('text.txt', 'A.txt')
#8
def delete_file(path):
    if os.path.exists(path):
        if os.access(path, os.W_OK):
            os.remove(path)
            print(f"Файл {path} удалён")
        else:
            print("Нет прав на удаление")
    else:
        print("Файл не существует")

delete_file('B.txt')