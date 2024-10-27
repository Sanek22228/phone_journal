import json

file_path = "phone_dict.json"

# with open(file_path, "w") as json_file:
#     json.dump({}, json_file)

with open('phone_dict.json', 'r', encoding='utf-8') as json_file:
    global phone_dict
    phone_dict = json.load(json_file)

log_reg = True

def save_to_dict():
    with open("phone_dict.json", "w") as json_file:
        json.dump(phone_dict, json_file)

def display_dict(user):
    for i in phone_dict[user]["phone_dict"]:
        print(i, ":", str(phone_dict[user]["phone_dict"][i]))
    if phone_dict[user]["phone_dict"] == {}:
        print("\nУ вас пока что нет контактов\n")
    

def add_contact(user, name, number):
    phone_dict[user]["phone_dict"][name] = number
    print("Контакт добавлен")
    save_to_dict()

def del_contact(user, contact_name):
    if contact_name in phone_dict[user]["phone_dict"]:
        del phone_dict[user]["phone_dict"][contact_name]
        print("Контакт удален")
    else:
        print("Контакт не был найден")

def user_log_in():
    print("Авторизация\n")
    log = True
    while(log):
        login = input("Введите логин: ")
        password = input("Введите пароль: ")

        if login in phone_dict and password == phone_dict[login]["password"]:
            process(login)
            log = False
        else:
            print("Логин или пароль неправильный. Попробуйте еще раз.")

def process(user):
    do = True
    while(do):
        print("Просмотреть контакты - 'r'; Добавить контакт - 'a'; Удалить контакт - 'd';\nИзменить контакт - 'e'; Завершить сеанс - 'q'")
        choice = input("Введите команду: ")
        match choice:
            case "r":
                display_dict(user)
            case "a":
                contact_name = input("Введите имя контакта: ")
                contact_number = input("Ввелите номер контакта: ")
                add_contact(user, contact_name, contact_number)
            case "d":
                contact_name = input("Введите имя контакта для удаления: ")
                del_contact(user, contact_name)
            case "e":
                contact_name = input("Введите имя изменяемого контакта: ")
                contact_edited = input("Введите новые имя или номер контакта (имя : номер): ")
                edited_name = contact_edited.split(":")[0]
                if edited_name in phone_dict[user]["phone_dict"]:
                    phone_dict[user]["phone_dict"][edited_name] = contact_edited.split(":")[1:]
                else:
                    del_contact(user, contact_name)
                    phone_dict[user]["phone_dict"][edited_name] = contact_edited.split(":")[0]
                save_to_dict()
            case "q":
                do = False
            case _:
                print("hell nah")

while log_reg:

    print(phone_dict)
    print("Для выхода из программы введите 'q'")
    user_log_or_reg = input("Войти в аккаунт или зарегистрировать новый? (l/r): ")

    if (user_log_or_reg == "l" or user_log_or_reg == "L" or user_log_or_reg == "д" or user_log_or_reg == "Д") and phone_dict != {}:
        user_log_in()        

    elif user_log_or_reg == "r" or user_log_or_reg == "R" or user_log_or_reg == "к" or user_log_or_reg == "К":
        print("Регистрация")

        reg = True

        while(reg):
            login = input("Введите логин: ")
            password = input("Введите пароль: ")
            subm_password = input("Подтвердите пароль: ")
            if password == subm_password:
                print("Аккаунт зарегистрирован")
                password = {"password" : password, 
                            "phone_dict" : {}}
                phone_dict[login] = password
                save_to_dict()
                process(login)
                reg = False

    elif user_log_or_reg == "q" or user_log_or_reg == "Q" or user_log_or_reg == "й" or user_log_or_reg == "Й":
        print("Выход из программы")
        log_reg = False

    else:
        print("Введене некорректная команда. Попробуйте еще")