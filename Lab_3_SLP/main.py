from func_lab3 import *

def main():  
    create_file()  # створення файлу
    checking_for_an_empty_list()  # перевірка чи файл порожній

    while True:
        сhoice = show_menu() # виведення меню
        if сhoice == 1:
            input_name = input("Введіть ім'я і прізвище студента: ")
            input_score = input("Введіть середній бал студента: ")

            students_KN = [(input_name, input_score)]
            add_student_KN(students_KN)
            print("Дані успішно додані")
            if continuation() == False:
                break
            else:
                continue
        
        elif сhoice == 2:
            input_name = input("Введіть номер студента, якого ви хочете видалити: ")
            delete_student_KN(input_name)
            print("Студент успішно видалений") 
            
            if continuation() == False:
                break
            else:
                continue

        elif сhoice == 3:
            input_name = input("Введіть номер студента, якого ви хочете редагувати: ")
            input_new_name = input("Введіть нове прізвище і ім'я студента: ")
            input_new_score = input("Введіть новий середній бал студента: ")
            edit_student_KN(input_name, input_new_name, input_new_score)
            print("Дані успішно відредаговані")
            
            if continuation() == False:
                break
            else:
                continue

        elif сhoice == 4:
            show_students_KN()
            if continuation() == False:
                break
            else:
                continue

        elif сhoice == 5:
            sort_students_KN()
            print("Дані успішно відсортовані")
            if continuation() == False:
                break
            else:
                continue
            
        elif сhoice == 6:
            input_name = input("Введіть прізвище і ім'я студента, якого ви хочете знайти: ")
            search_student_KN(input_name)
            if continuation() == False:
                break
            else:
                continue

        elif сhoice == 7:
            print("Дякую за роботу!")
            break

        else:
            print("Некоректний ввід. Введіть число від 1 до 7.")

if __name__ == "__main__":
     main()