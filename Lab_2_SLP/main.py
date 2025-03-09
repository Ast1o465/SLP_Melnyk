from function import *

def main():
    lab_2 = { # словник з функціями
        1: "Визначити пору року за номером місяця",
        2: "визначити чи високосний рік",
        3: "визначити чи існує така дата",
        4: "визначити чи є однакові дати в списку",
        5: "випадкова дата в форматі dd.mm.yyyy",
        6: "різниця між двома датами",
        7: "виводить місяць за номером", 
    }
    print("Меню програми:")
    for key, value in lab_2.items():# виведення меню
        print(f"{key}. {value}")

    choice = (input("\nВиберіть пункт меню: "))

    if not choice.isdigit(): # перевірка чи введене число
        print("Номер повинен бути числом від 1 до 7")
        return
    
    choice = int(choice)# переведення введеного значення в число

    if choice not in lab_2:
        print("Немає функцій для виконання")

    elif choice == 1:   
        n = int(input("Введіть номер місяця: "))
        print("Пора року:", number_of_month(n))

    elif choice == 2:
        n = int(input("Введіть рік: "))
        if number_year(n):
            print("цей рік високосний") 
        else: 
            print("цей рік не високосний")

    elif choice == 3:
        day = int(input("Введіть день: "))
        month = int(input("Введіть місяць: "))
        year = int(input("Введіть рік: "))

        check_date_exists(day, month, year)

        if check_date_exists(day, month, year):
            print("така дата існує")
        else:
            print("такої дати не буває")

    elif choice == 4:
        all_dates = []
        while True: # цикл для введення дат
            input_date = input("введіть дату у форматі dd.mm.yyyy: ") # введення дати

            if input_date == "": # якщо дата не введена
                break # вихід з програми
        
            all_dates.append(input_date) # додаємо введену дату в загальний список
        
        duplicate_dates = list_date(all_dates) # отримуємо словник повторюваних дат
        
        if duplicate_dates: # якщо є повторювані дати
            print("Знайдені дублікати:")
            for date, count in duplicate_dates.items():
                print(f"Дата {date} зустрічається {count} разів")
        else:
            print("Дублікатів не знайдено")
        print() 
        
    elif choice == 5:

        number_random_year ={
            1: "Генерувати 1 рандомну дату",
            2: "Генерувати 2 рандомні дати",
            3: "Генерувати 3 рандомні дати",
            4: "Генерувати 4 рандомні дати",
            5: "Генерувати 5 рандомних дат",
        }
            
        print("Меню програми:")
        for key, value in number_random_year.items():# виведення меню
            print(f"{key}. {value}")

        choice = (input("\nВиберіть пункт меню: "))

        if not choice.isdigit(): # перевірка чи введене число
            print("Номер повинен бути числом від 1 до 5")
            return

        if choice == "1":
            print("Рандомна дата:", random_date())
        elif choice == "2":
            for i in range(2):
                print("Рандомна дата:", random_date())
        elif choice == "3":
            for i in range(3):
                print("Рандомна дата:", random_date())
        elif choice == "4":
            for i in range(4):
                print("Рандомна дата:", random_date())
        elif choice == "5":
            for i in range(5):
                print("Рандомна дата:", random_date())
        else:
            print("Немає функції для виконання")

    elif choice == 6:

        select_a_filling ={
            1: "Ввести дати",
            2: "Ввести рандомні дати",
        }
        
        print("Меню програми:")
        for key, value in select_a_filling.items():# виведення меню
            print(f"{key}. {value}")

        choice = (input("\nВиберіть пункт меню: "))

        if not choice.isdigit(): # перевірка чи введене число
            print("Номер повинен бути числом від 1 до 2")
            return
        
        if choice == "1":
            date1 = input("Введіть першу дату у форматі dd.mm.yyyy: ")
            date2 = input("Введіть другу дату у форматі dd.mm.yyyy: ")

            print("Різниця між датами:", difference_dates(date1, date2))

        elif choice == "2":
            # date1 = print(random_date())
            # date2 = print(random_date())
            print(difference_dates(random_date(), random_date()))
        else:
            print("Немає функції для виконання")    

    elif choice == 7:
        n = int(input("Введіть номер місяця: "))
        print("Місяць:", month_name(n))
    else:
        print("Немає функції для виконання")
    
if __name__ == "__main__": # Перевірка чи файл був запущений напряму
    main()