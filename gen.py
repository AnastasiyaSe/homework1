# with open(r"C:\Users\Анастасия\PycharmProjects\netology\venv\file.txt", "r") as f:
#    lines = f.readlines()
#    print(lines)

import hashlib
def gen(path):

      with open(rf"{path}", "r") as f:
         lines = f.readlines()
         for line in lines:
            yield hashlib.md5(line.encode()).hexdigest()

path = input('Введите путь до файла: ')

generator = gen(path)
print(generator)


