import yadisk
import pathlib
from pathlib import Path

# Получаем строку, содержащую путь к рабочей директории:
dir_path = pathlib.Path.cwd()
path = Path(dir_path, 'token', 'tokenYa.txt')
print(path)

with open(r'E:\Py\PY_Advance\6_Function_Tests\token\tokenYa.txt', 'r', ) as fileYA:
    tokenYA = fileYA.read()
Ya = yadisk.YaDisk(token=tokenYA)

#  Почему в-т ниже не видит путь при запуске test_Pytest?

# with open(path, 'r', ) as fileYA:
#     tokenYA = fileYA.read()
# Ya = yadisk.YaDisk(token=tokenYA)


def make_dir(name):
    try:
        Ya.mkdir(path=name)
        return True
    except yadisk.exceptions.DirectoryExistsError:
        return False

def del_dir(name):
    try:
        Ya.remove(path=name)
        return True
    except yadisk.exceptions.PathNotFoundError:
        return False

if __name__ == '__main__':
    print(make_dir('777'))
    print(del_dir('777'))
