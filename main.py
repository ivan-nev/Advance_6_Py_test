# Я работаю секретарем и мне постоянно приходят различные документы. Я должен быть очень внимателен чтобы не потерять ни один документ. Каталог документов хранится в следующем виде:

documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]
# Перечень полок, на которых находятся документы хранится в следующем виде:

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


def all_num():
    list_num = []
    for doc in documents:
        list_num += [doc['number']]
    return list_num


# p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
def get_name_in_number(number_):
    for document in documents:
        # print(type(document))
        if document['number'] == number_:
            return document['name']
    return "Номер не найден"


# print (get_name_in_number(11-2))

# s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
# Правильно обработайте ситуации, когда пользователь будет вводить несуществующий документ.

def get_num_shelf_in_num(number):
    for key, num_doc in directories.items():
        if number in num_doc:
            return key
    return 'Номер документа не найден'


# l– list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";

def get_list():
    str_list = ''
    for doc in documents:
        str_list += f'''{doc['type']} "{doc['number']}" "{doc['name']}"\n'''
    return str_list

    # a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться. Корректно обработайте ситуацию, когда пользователь будет пытаться добавить документ на несуществующую полку.

def add_new_doc():
    new_line = {}
    new_line['type'] = input('Введите тип: ')
    new_line['number'] = input('Введите номер: ')
    new_line['name'] = input('Введите имя: ')
    shelf = None
    while shelf not in directories.keys():
        shelf = input(f'Выберете полку {str(list(directories.keys()))}: ')
        if shelf in directories.keys():
            break
        print('Нет такой')
    documents.append(new_line)
    directories[shelf] = list(directories[shelf]) + [new_line['number']]
    return True


# as – add shelf – команда, которая спросит номер новой полки и добавит ее в перечень. Предусмотрите случай, когда пользователь добавляет полку, которая уже существует.;

def add_shelf(num_shelf):
    if num_shelf not in directories.keys():
        directories[num_shelf] = []
        print('Полка добавлена')
        return True
    else:
        print('Полка уже есть')
        return False


# d – delete – команда, которая спросит номер документа и удалит его из каталога и из перечня полок. Предусмотрите сценарий, когда пользователь вводит несуществующий документ;
def del_doc(num_doc):
    for i, doc in enumerate(documents):
        if doc['number'] == num_doc:
            del documents[i]
            for key, num_ in directories.items():
                if num_doc in num_:
                    directories[key].remove(num_doc)
                    print(f'Документ номер: {num_doc} удалён')
                    return True
    print(f'Документ номер: {num_doc} не существует')
    return False


# m – move – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую. Корректно обработайте кейсы, когда пользователь пытается переместить несуществующий документ или переместить документ на несуществующую полку;

def move_doc(num_doc, num_dir):
    dict_copy = directories.copy()
    if num_dir in dict_copy.keys():
        for key, number in dict_copy.items():
            if num_doc in number:
                number.remove(num_doc)
                directories[key] = number
                directories[num_dir] += [num_doc]
                print(f'Документ {num_doc} перенесён из полки {key} на полку {num_dir}')
                return True
        print('Не верный ном документа')
        return False
    else:
        print('Нет папки назначения')
        return False

def start():
    """
    ap - (all people) - команда, которая выводит список всех владельцев документов
    p – (people) – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
    l – (list) – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
    s – (shelf) – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
    a – (add) – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип,
    имя владельца и номер полки, на котором он будет храниться.
    d – (delete) – команда, которая спросит номер документа и удалит его из каталога и из перечня полок;
    m – (move) – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую;
    as – (add shelf) – команда, которая спросит номер новой полки и добавит ее в перечень;
    q - (quit) - команда, которая завершает выполнение программы
    """
    print(
        'Вас приветствует программа помошник!\n',
        '(Введите help, для просмотра списка поддерживаемых команд)\n'
    )
    while True:
        print()
        command = input('Ведите команду: ')
        print()
        if command == "p":
            print(get_name_in_number(input(f'Введите ном. докум {all_num()}: ')))
        elif command == "s":
            n = get_num_shelf_in_num(input(f'Введите ном. докум {all_num()}: '))
            print(f'Номер полки {n}')
        elif command == "l":
            print(get_list())
        elif command == "a":
            add_new_doc()
        elif command == "as":
            add_shelf(input('Введите ном новой полки: '))
        elif command == "d":
            del_doc(input(f'Введите ном. докум для удал {all_num()}: '))
        elif command == "m":
            n = input(f'Ведите ном. докум {all_num()}: ')
            p = input(f'Куда перенести {str(list(directories.keys()))}: ')
            move_doc(n, p)
        elif command == 'pr':
            print(documents)
            print(directories)
        elif command == 'help':
            print(start.__doc__)
        else:
            print('Не верная команда')

if __name__ == '__main__':
    start()


