import random as rand
import datetime as dati

def number_of_month(n):
    """
    Функцію, що приймає 1 аргумент – номер місяця (від 1 до 12),
    і повертає пору року, якому цей місяць належить (зима, весна, літо чи осінь).
    """
    if not (1 <= n <= 12): # перевірка чи номер місяця від 1 до 12
        return "Номер місяця повинен бути від 1 до 12"
    elif n == 12 or n == 1 or n == 2: 
        return "зима"
    elif n >= 3 and n <= 5:
        return "весна"
    elif n >= 6 and n <= 8: 
        return "літо"
    else:
        return "осінь"
    

def number_year(n):
    """
    Функцію, яка приймає 1 аргумент – номер року,
    і повертає True, якщо рік високосний, і False інакше. 
    Примітка: Будь-який рік, який ділиться на 4 без залишку, 
    є високосним роком: наприклад, 1988, 1992 та 1996 роки є високосними
    """
    if n % 4 == 0:  # якщо рік ділиться на 4
        return True # то це високосний рік
    else:
        return False # інакше це не високосний рік

def check_date_exists(day, month, year):
    """
    Функцію, що приймає 3 аргументи – день, місяць та рік.
    Повернути True, якщо така дата існує, та False – якщо такої дати не буває
    (наприклад 15-тий місяць);
    """
    if month < 1 or month > 12: # перевірка чи місяць від 1 до 12
        return False # якщо ні, то такої дати не буває
    
    if month == 2: # якщо місяць лютий
        if number_year(year): # перевірка чи це високосний рік
            return 1 <= day <= 29 # якщо так, то 29 днів
        else:
            return 1 <= day <= 28 # якщо ні, то 28 днів
        
    if month in [1, 3, 5, 7, 8, 10, 12]: # якщо місяць має 31 день
        return 1 <= day <= 31 # то день повинен бути від 1 до 31
    else:
        return 1 <= day <= 30 # інакше день повинен бути від 1 до 30
    
def list_date(dd_mm_yyyy):
    """
    Функцію, що як аргумент отримує список дат у форматі dd.mm.yyyy 
    (наприклад, ["11.12.1877", "25.01.2022", "01.05.2023"]) 
    і шукає у ньому повтори, якщо повтори є – повертає словник з датами та кількістю їх повторень
    """
    dates_vocabulary = {} # словник для зберігання дат
    
    for date in dd_mm_yyyy: # перебір дат
        # Перевіряємо формат дати
        parts = date.split('.') # розділяємо дату на частини
        if len(parts) != 3: # якщо дата не має трьох частин
            print(f"Неправильний формат дати: {date}") # виводимо повідомлення
            continue
        
        # Розбиваємо дату на день, місяць та рік
        day, month, year = map(int, parts)
        
        # Перевіряємо, чи існує така дата
        if check_date_exists(day, month, year):
            # Якщо дата існує, додаємо її до словника
            if date in dates_vocabulary:
                dates_vocabulary[date] += 1
            else:
                dates_vocabulary[date] = 1
        else:
            print(f"Дата {date} не існує і була пропущена")
    
    result = {} # словник для зберігання дат, які повторюються, та кількості їх повторень
    
    for date, count in dates_vocabulary.items(): # перебір дат та їх кількості
        if count > 1: # якщо дата повторюється
            result[date] = count  # додаємо дату та кількість повторень в словник
    
    if result:
        print("Знайдені дублікати дат")
    else:
        print("Дублікатів не знайдено")
        
    return result # повертаємо словник дат, які повторюються, та кількості їх повторень

def random_date():
    """
    Функцію, у якої немає аргументів, а повертає вона випадкову дату у форматі dd.mm.yyyy.
    """
    day = rand.randint(1, 31) # випадковий день
    month = rand.randint(1, 12) # випадковий місяць
    year = rand.randint(1900, 2030) # випадковий рік
    
    if month == 2:
        if number_year(year): 
            day = rand.randint(1, 29) 
        else:
            day = rand.randint(1, 28) 
    elif month in [4, 6, 9, 11]:
        day = rand.randint(1, 30)  
    else:
        day = rand.randint(1, 31)

    return f"{day:02d}.{month:02d}.{year}" # повертаємо дату у форматі dd.mm.yyyy 
    

def difference_dates(date1, date2):
    """
    Функцію, що отримує як аргументи дві дати (формат обрати самостійно)
    та повертає кількість днів між ними. Примітка: Використати 
    бібліотеку datetime та її функцію з такою ж назвою datetime.
    """
    # Перевірка формату дат
    if date1.count('.') != 2 or date2.count('.') != 2:
        print("Помилка: дати повинні бути у форматі dd.mm.yyyy")
        return None
    
    # Розділяємо дати на компоненти
    date1_parts = date1.split('.')
    date2_parts = date2.split('.')
    
    # Перевірка, чи всі компоненти є числами
    is_valid_format = True
    for part in date1_parts + date2_parts:
        if not part.isdigit():
            is_valid_format = False
            break
    
    if not is_valid_format:
        print("Помилка: компоненти дати повинні бути числами")
        return None
    
    # Конвертуємо компоненти в цілі числа
    day1, month1, year1 = map(int, date1_parts)
    day2, month2, year2 = map(int, date2_parts)
    
    # Перевірка існування дат
    if not check_date_exists(day1, month1, year1):
        print("Помилка:  дата введена неправильно")
        return None
    if not check_date_exists(day2, month2, year2):
        print("Помилка:  дата введена неправильно")
        return None
    
    # Перетворюємо коректні дати у об'єкти datetime
    date1_dt = dati.datetime.strptime(date1, "%d.%m.%Y")
    date2_dt = dati.datetime.strptime(date2, "%d.%m.%Y")
    
    # Визначаємо послідовність дат і виводимо їх
    if date1_dt <= date2_dt:
        print(f"Дата 1: {date1}")
        print(f"Дата 2: {date2}")
        difference = date2_dt - date1_dt
    else:
        print(f"Дата 1: {date2}")
        print(f"Дата 2: {date1}")
        difference = date1_dt - date2_dt
    
    # Повертаємо кількість днів між датами
    return difference.days


def month_name(n):
    """
    отримує як аргумент номер місяця, виводить на екран 
    відповідну назву місяця та нічого не повертає.
    """
    months = { # словник з назвами місяців
        1: "Січень",
        2: "Лютий",
        3: "Березень",
        4: "Квітень",
        5: "Травень",
        6: "Червень",
        7: "Липень",
        8: "Серпень",
        9: "Вересень",
        10: "Жовтень",
        11: "Листопад",
        12: "Грудень"
    }
    return months.get(n, "Такого місяця не існує")