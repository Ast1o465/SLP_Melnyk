import csv
import os

file_created = False  # перемінна для перевірки чи файл був створений

def create_file():  
    """
    Функція для створення файлу, якщо він ще не існує
    """
    global file_created
    
    # якщо файл вже був створений, то вихід з функції
    if file_created:
        return
        
    if not os.path.exists('KN-24.csv'):
        with open('KN-24.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["№" , "ім'я", "Середній бал"])
            print("Файл 'KN-24.csv' успішно створено")
    else:
        print("Файл 'KN-24.csv' вже існує")
    
    file_created = True  # файл був створений
    
def checking_for_an_empty_list():
    """
    Функція для перевірки чи файл порожній
    """
    # Перевіряємо, чи файл порожній (крім заголовка)
    with open('KN-24.csv', 'r', newline='', encoding='utf-8') as file:
        students = list(csv.reader(file))
        file_is_empty = len(students) <= 1
    
    # Додаємо студентів тільки якщо файл порожній або містить лише заголовок
    if file_is_empty:
        names = ["Балановська Анастасія", "Безай Роман", "Безкровна Вероніка", 
                "Булюкін Володимир", "Громов Іван", "Гладкий Іван",
                "Данилюк Максим", "Дмитренко Ярослава", "Дуднік Микита", 
                "Дяков Данило", "Калініченко Михайло", "Коваленко Артем", 
                "Ковальов Данило", "Ковальова Єва", "Колодонос Андрій",
                "Куріщенко Павло", "Куртяк Катерина", "Малецький Микита",
                "Маслова Вероніка", "Мельник Дмитро", "Мироненко Ярослав",
                "Мойсейченко Максим", "Немненко Максим", "Олексенко Артем",
                "Павлишин Денис", "Приймак Данило" , "Радомська Діана",
                "Разумний Андрій", "Середа Марина", "Стрижеус Віталій",
                "Терещенко Владислав", "Червонець Артем"] # ім'я студента
        
        students_KN = [(name, ran_e()) for name in names] # створення списку студентів
        add_student_KN(students_KN) # додавання студентів у файл

def ran_e():
    """
    Функція для генерації випадкового числа від 60 до 100
    """
    import random
    return round(random.uniform(60.0, 99.0), 1)

def add_student_KN(students_KN):
    """
    Функція для додавання студентів 
    у файл і нумерації їх
    і ставе номер останій + 1
    """
    if not os.path.exists('KN-24.csv'):
        create_file()
        
    with open('KN-24.csv', 'r', newline='', encoding='utf-8') as file:
        students = list(csv.reader(file))
        
    with open('KN-24.csv', 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Перевіряємо, чи є у файлі рядки даних окрім заголовку
        if len(students) > 1:
            number = int(students[-1][0]) + 1
        else:
            # Якщо у файлі тільки заголовок, починаємо нумерацію з 1
            number = 1
        for student in students_KN:
            writer.writerow([number, student[0], student[1]])
            number += 1


def delete_student_KN(number):
    """     
    Функція для видалення студента
    і настроює нумерацію щоб вона була правильною
    """
    if not os.path.exists('KN-24.csv'):
        print("Помилка: файл не існує. Спочатку створіть файл.")
        return
        
    with open('KN-24.csv', 'r', newline='', encoding='utf-8') as file:
        students = list(csv.reader(file))

        number_str = str(number)
       
        new_students = [students[0]]  
        current_num = 1

        for student in students[1:]:
            if student[0] != number_str:
                student[0] = str(current_num)
                new_students.append(student)
                current_num += 1
      
    with open('KN-24.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for student in new_students:
            writer.writerow(student)

def edit_student_KN(number, new_name, new_score):
    """
    Функція для редагування студента
    """
        
    with open('KN-24.csv', 'r', newline='', encoding='utf-8') as file:
        students = list(csv.reader(file))

        number_str = str(number)
        new_students = [students[0]]  
        for student in students[1:]:
            if student[0] == number_str:
                student[1] = new_name
                student[2] = new_score
            new_students.append(student)
      
    with open('KN-24.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for student in new_students:
            writer.writerow(student)

def continuation():
    """
    Функція для продовження роботи програми
    """
    answer = input("Продовжити роботу? (так/ні): ")
    if answer == "так":
        return True
    elif answer == "ні":
        return False
    else:
        print("Некоректний ввід. Введіть 'так' або 'ні'.")

def show_students_KN():
    """
    Функція для виведення списку студентів
    """
    with open('KN-24.csv', 'r', newline='', encoding='utf-8') as file:
        students = list(csv.reader(file))
        for student in students[1:]:
            print(f"{student[0]}. {student[1]} - {student[2]}")

def sort_students_KN():
    """
    Функція для сортування студентів за середнім балом
    """
    with open('KN-24.csv', 'r', newline='', encoding='utf-8') as file:
        students = list(csv.reader(file))
        header = students[0]  # Зберігаємо заголовок
        data = students[1:]   # Дані студентів
        
        # Сортування студентів за середнім балом
        data.sort(key=lambda x: float(x[2]), reverse=True)
    
    with open('KN-24.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        for student in data:
            writer.writerow(student)

def search_student_KN(input_name):
    """
    Функція для пошуку студента за прізвищем і ім'ям
    """
    with open('KN-24.csv', 'r', newline='', encoding='utf-8') as file:
        students = list(csv.reader(file))
        for student in students[1:]:
            if input_name == student[1]:
                print(f"{student[0]}. {student[1]} - {student[2]}")
                return
        print("Студент не знайдений")

def show_menu():
    """
    Функція для виведення меню
    """
    select = {
        1: "Додати нового студента",
        2: "Видалити студента",
        3: "Редагувати студента",
        4: "Показати список студентів",
        5: "сортування студентів за середнім балом",
        6: "Пошук студента за прізвищем і ім'ям",
        7: "Вихід з програми"
    }
    
    print("Меню програми:")
    for key, value in select.items():  # виведення меню
        print(f"{key}. {value}")

    choice = int(input("\nВиберіть пункт меню: "))
    return choice