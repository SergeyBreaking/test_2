def open_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print("Файл не найден.")

def save_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)
        print("Файл сохранен.")

def main():
    while True:
        print("1 - Открыть файл")
        print("2 - Сохранить файл")
        print("3 - Выйти")
        choice = input("Выберите действие: ")

        if choice == '1':
            filename = input("Введите имя файла для открытия: ")
            content = open_file(filename)
            print(content)
        elif choice == '2':
            filename = input("Введите имя файла для сохранения: ")
            content = input("Введите текст для сохранения: ")
            save_file(filename, content)
        elif choice == '3':
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")

if __name__ == '__main__':
    main()