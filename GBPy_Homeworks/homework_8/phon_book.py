def data_one():    # Начало работы со справочником
    print('Возможны следующие операции со справочником: \n'
          '1 - добавление информации в справочник; \n'
          '2 - вывод содержимого справочника \n'
          '3 - поиск абонента \n'
          '4 - завершение работы \n')      
    operation = 0 
    while operation != '4':
        operation = input('Укажите режим работы с телефонным справочником: ')
        if operation == '1':
            user_data = input_data()
            add_user(phone_book, user_data)
            write_txt('phone_book.txt', phone_book)
        elif operation == '2':
            print_directory(phone_book)
        elif operation == '3':
            search_data()
        elif operation == '4':
            break    
        else:
            print('Введено не корректное значение: ')

def input_data() -> list:  # Создание списка данных абонента 
    print('Требуется создать карточку абонента.')
    new_user = []
    new_user.append(input('Введите фамилию: ').title())
    new_user.append(input('Введите имя: ').title())
    new_user.append(input('Введите отчество: ').title())
    new_user.append(input('Введите телефон: '))
    return new_user

def add_user(phone_book, user_data): # Создание новой строки данных абонента в справочнике
    phone_book.append({'Фамилия': f'{user_data[0]}', 'Имя': f'{user_data[1]}',
                      'Отчество': f'{user_data[2]}', 'Телефон': f'{user_data[3]}'})  

def read_txt(filename: str) -> list:  # Чтение текстового файла
    data = []
    fields = ["Фамилия", "Имя", "Отчество", "Телефон"]
    with open(filename, 'r', encoding='utf-8') as file_2:
        for line in file_2:
            record = dict(zip(fields, line.strip().split(',')))
            data.append(record)
    return data

def write_txt(filename: str, data: list):
    with open(filename, 'w', encoding='utf-8') as file_1:
        for i in range(len(data)):
            s = ''
            for j in data[i].values():
                s += j + ','
            file_1.write(f'{s[:-1]}\n')

phone_book = read_txt('phone_book.txt')

def print_directory(data: list) -> None:
    print('\nСправочник абонентов (Фамилия, Имя, Отчество, Телефон):\n')
    for line in data:
        str_1 = ''
        for el in line:
            str_1 += line[el] + ' '
        print(str_1)

def search_data():
    print('Поиск может осуществляться при введении следующих данных \n'
          '1 - Имя абонента \n'
          '2 - Фамилии абонента \n'
          '3 - Имя и фамилия абонента \n'
          '4 - Номер телефона абонента \n'
          '5 - Выход из режима поиска \n')
    search = 0
    while search != '5':
        search = input('Введите предпочитаемый вариант поиска абонента: ')
        if search == '1':
            name = get_search_name()
            print(* find_by_name(phone_book, name))
        elif search == '2':
            suname = get_search_suname()
            print(* find_by_suname(phone_book, suname))
        elif search == '3':
            name = get_search_name()
            suname = get_search_suname()
            print(* find_by_suname_name(phone_book, suname, name))
        elif search == '4':
            number_phone = get_search_number_phone()
            print(* find_by_number_phone(phone_book, number_phone))
        elif search == '5':
            break

def get_search_name():
    return input('\nВведите имя для поиска: ').title()

def find_by_name(phone_book: list, name: str) -> str:
    result = []
    for line in phone_book:
        if name == line['Имя']:
            result.append(line['Фамилия'])
            result.append(line['Имя'])
            result.append(line['Отчество'])
            result.append(line['Телефон'] + '\n')
    if (len(result) == 0):
        return 'None'
    else:
        return result

def get_search_suname():
    return input('\nВведите фамилию для поиска: ').title()

def find_by_suname(phone_book: list, suname: str) -> str:
    result = []
    for line in phone_book:
        if suname == line['Фамилия']:
            result.append(line['Фамилия'])
            result.append(line['Имя'])
            result.append(line['Отчество'])
            result.append(line['Телефон'] + '\n')
    if (len(result) == 0):
        return 'None'
    else:
        return result

def find_by_suname_name(phone_book: list, suname: str, name: str) -> str:
    result = []
    for line in phone_book:
        if suname == line['Фамилия'] and name == line['Имя']:
            result.append(line['Фамилия'])
            result.append(line['Имя'])
            result.append(line['Отчество'])
            result.append(line['Телефон'] + '\n')
    if (len(result) == 0):
        return 'None'
    else:
        return result

def get_search_number_phone():
    return input('\nВведите номер телефона для поиска абонента: ')

def find_by_number_phone(phone_book: list, number_phone: str) -> str:
    result = []
    for line in phone_book:
        if number_phone == line['Телефон']:
            result.append(line['Фамилия'])
            result.append(line['Имя'])
            result.append(line['Отчество'])
            result.append(line['Телефон'] + '\n')
    if (len(result) == 0):
        return 'None'
    else:
        return result

data_one()


