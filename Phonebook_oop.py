import csv
from typing import List


class Phonebook:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def add_record(self) -> None:
        with open(self.filename, 'a', newline='') as file:
            writer = csv.writer(file)
            surname = input("Введите фамилию: ")
            name = input("Введите имя: ")
            patronymic = input("Введите отчество: ")
            organization = input("Введите название организации: ")
            work_phone = input("Введите рабочий телефон: ")
            personal_phone = input("Введите личный телефон: ")
            writer.writerow([surname, name, patronymic, organization, work_phone, personal_phone])

    def edit_record(self) -> None:
        records = self.read_records()
        surname = input("Введите фамилию для редактирования: ")
        for i, record in enumerate(records):
            if record[0] == surname:
                print(f"Найдена запись: {record}")
                new_record = input("Введите новую запись через запятую "
                                   "(фамилия, имя, отчество, организация, рабочий телефон,"
                                   " личный телефон): ").split(',')
                records[i] = new_record
                break
        self.write_records(records)

    def search_records(self, search_term: str) -> List[List[str]]:
        records = self.read_records()
        found_records = [record for record in records if search_term in record]
        return found_records

    def read_records(self) -> List[List[str]]:
        with open(self.filename, 'r') as file:
            reader = csv.reader(file)
            return list(reader)

    def write_records(self, records: List[List[str]]) -> None:
        with open(self.filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(records)

    def print_records(self, page_size: int = 10) -> None:
        records = self.read_records()
        page = 0
        while page * page_size < len(records):
            print(f"Страница {page + 1}")
            for record in records[page * page_size:(page + 1) * page_size]:
                print(record)
            input("Нажмите Enter для продолжения...")
            page += 1


def main() -> None:
    phonebook = Phonebook('phonebook.csv')
    while True:
        print("\nТелефонный справочник")
        print("1. Вывод постранично записей из справочника на экран")
        print("2. Добавление новой записи в справочник")
        print("3. Редактирование записей в справочнике")
        print("4. Поиск записей по одной или нескольким характеристикам")
        print("5. Выход")
        choice = input("Выберите действие: ")
        if choice == '1':
            phonebook.print_records()
        elif choice == '2':
            phonebook.add_record()
        elif choice == '3':
            phonebook.edit_record()
        elif choice == '4':
            search_term = input("Введите термин для поиска: ")
            found_records = phonebook.search_records(search_term)
            for record in found_records:
                print(record)
        elif choice == '5':
            break
        else:
            print("Неверный выбор. Попробуйте еще раз.")


if __name__ == "__main__":
    main()
