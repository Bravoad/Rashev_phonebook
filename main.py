import csv


# Функция для добавления новой записи в справочник


def add_record(filename: str) -> None:
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        surname = input("Введите фамилию: ")
        name = input("Введите имя: ")
        patronymic = input("Введите отчество: ")
        organization = input("Введите название организации: ")
        work_phone = input("Введите рабочий телефон: ")
        personal_phone = input("Введите личный телефон: ")
        writer.writerow([surname, name, patronymic, organization, work_phone, personal_phone])


# Функция для редактирования записи в справочнике


def edit_record(filename: str) -> None:
    records = read_records(filename)
    surname = input("Введите фамилию для редактирования: ")
    for i, record in enumerate(records):
        if record[0] == surname:
            print(f"Найдена запись: {record}")
            new_record = input("Введите новую запись через запятую "
                               "(фамилия, имя, отчество, организация, рабочий телефон,"
                               " личный телефон): ").split(',')
            records[i] = new_record
            break
    write_records(filename, records)


# Функция для поиска записей по одной или нескольким характеристикам


def search_records(filename: str, search_term: str) -> list:
    records = read_records(filename)
    found_records = [record for record in records if search_term in record]
    return found_records


# Функция для чтения записей из файла


def read_records(filename: str) -> list:
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        return list(reader)


# Функция для записи записей в файл


def write_records(filename: str, records: list) -> None:
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(records)


# Функция для вывода постранично записей из справочника на экран


def print_records(filename: str, page_size: int = 10) -> None:
    records = read_records(filename)
    page = 0
    while page * page_size < len(records):
        print(f"Страница {page + 1}")
        for record in records[page * page_size:(page + 1) * page_size]:
            print(record)
        input("Нажмите Enter для продолжения...")
        page += 1


# Главная функция для управления справочником


def main() -> None:
    filename = 'phonebook.csv'
    while True:
        print("\nТелефонный справочник")
        print("1. Вывод постранично записей из справочника на экран")
        print("2. Добавление новой записи в справочник")
        print("3. Редактирование записей в справочнике")
        print("4. Поиск записей по одной или нескольким характеристикам")
        print("5. Выход")
        choice = input("Выберите действие: ")
        if choice == '1':
            print_records(filename)
        elif choice == '2':
            add_record(filename)
        elif choice == '3':
            edit_record(filename)
        elif choice == '4':
            search_term = input("Введите термин для поиска: ")
            found_records = search_records(filename, search_term)
            for record in found_records:
                print(record)
        elif choice == '5':
            break
        else:
            print("Неверный выбор. Попробуйте еще раз.")


if __name__ == "__main__":
    main()
