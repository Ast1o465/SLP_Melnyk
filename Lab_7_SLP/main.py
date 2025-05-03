import matplotlib.pyplot as plt  # Для побудови графіків
from collections import Counter  # Для підрахунку частоти елементів
import numpy as np               # Для роботи з масивами (використовується для позицій стовпців)
import os 

def task_1():       
    x = np.linspace(1, 10, 1000)
    y = 5 * np.sin(x) * np.cos((x**2 + 1/x)**2)

    plt.plot(x, y)
    plt.title("Y(x) = 5*sin(x)*cos((x^2 + 1/x)^2)")
    plt.xlabel("x")
    plt.ylabel("Y(x)")
    plt.grid()
    plt.savefig("Lab_7_SLP/graph.png")
    plt.show()
    print("Графік збережено у файл Lab_7_SLP/graph.png")

def task_2():
    """
    Зобразити гістограму частоти появи літер у тексті
    та зберегти у .png файл.
    """
    # Перевіряємо, чи існує файл 'Lab_7_SLP/text.txt'
    if not os.path.exists("Lab_7_SLP/text.txt"):
        print("Файл 'Lab_7_SLP/text.txt' не знайдено.")
        return

    # Відкриваємо файл 'Lab_7_SLP/text.txt' для читання з кодуванням utf-8
    with open("Lab_7_SLP/text.txt", "r", encoding='utf-8') as file:
        text = file.read() # Читаємо весь вміст файлу
        # Перевіряємо, чи файл не порожній
        if not text:
            print("Текстовий файл порожній.")
            return

    # Переводимо весь текст у нижній регістр для уніфікації підрахунку
    text = text.lower()

    # Видаляємо з тексту всі символи, крім літер
    cleaned_text = "".join(filter(str.isalpha, text))

    # Перевіряємо, чи залишились літери після очищення
    if not cleaned_text:
        print("У текстовому файлі не знайдено літер.")
        return

    # Підраховуємо частоту кожної літери
    letter_counts = Counter(cleaned_text)
    
    # Сортуємо літери за алфавітом для відображення на гістограмі
    sorted_items = sorted(letter_counts.items())
    # Розділяємо відсортовані пари (літера, частота) на два списки
    letters = [item[0] for item in sorted_items]     # Список літер
    frequencies = [item[1] for item in sorted_items] # Список відповідних частот

    # Перевіряємо, чи є дані для побудови графіка
    if not letters:
        print("Немає літер для побудови гістограми.")
        return

    # Створюємо масив позицій для стовпців на осі X
    x = np.arange(len(letters))

    plt.figure(figsize=(max(10, len(letters) * 0.4), 4)) # Встановлюємо ширину графіка в залежності від кількості літер
    plt.bar(x, frequencies, align='center')
    plt.xticks(x, letters)
    plt.xlabel("Літери")        # Підпис осі X
    plt.ylabel("Частота")       # Підпис осі Y
    plt.title("Гістограма частоти літер")
    plt.grid(axis='y', linestyle='--')
    plt.tight_layout()
    plt.savefig("Lab_7_SLP/letter_frequency_histogram.png")
    print("Гістограму збережено у файл Lab_7_SLP/letter_frequency_histogram.png")
    plt.show()

def task_3():
    """
    Зобразити гістограму частоти появи у певному
    тексті звичайних, питальних та окличних речень,
    а також речень, що завершуються трикрапкою та зберегти у .png файл.
    """

    if not os.path.exists("Lab_7_SLP/text.txt"):
        print("Файл 'Lab_7_SLP/text.txt' не знайдено.")
        return
    
    with open("Lab_7_SLP/text.txt", "r", encoding='utf-8') as file:
        text = file.read()
    if not text.strip():
        print("Текстовий файл порожній.")
        return
    
    # Підрахунок типів речень без регулярних виразів
    question_sentences = text.count('?')
    exclamatory_sentences = text.count('!')
    ellipsis_sentences = text.count('...')

    # Підрахунок звичайних речень (крапка, але не трикрапка)
    dot_count = text.count('.')
    if dot_count < ellipsis_sentences * 3:
        print("Некоректна кількість трикрапок у тексті.")
        return

    normal_sentences = dot_count - ellipsis_sentences * 3
   
    if all(count == 0 for count in [normal_sentences, question_sentences, exclamatory_sentences, ellipsis_sentences]):
        print("У тексті не знайдено жодного речення.")
        return

    # Дані для гістограми
    categories = ['Звичайне', 'Питальне', 'Окличне', 'Трикрапка']
    counts = [normal_sentences, question_sentences, exclamatory_sentences, ellipsis_sentences]

    # Створюємо нову фігуру для графіка
    plt.figure(figsize=(5, 5))
    plt.bar(categories, counts, color=['blue', 'green', 'red', 'orange'])
    plt.xlabel('Тип речення')
    plt.ylabel('Кількість')
    plt.title('Гістограма частоти типів речень')
    plt.grid(axis='y', linestyle='--')
    plt.tight_layout()
    plt.savefig("Lab_7_SLP/sentence_type_histogram.png")
    plt.show()
    
    # Зберігаємо гістограму у файл
    print("Гістограму збережено у файл Lab_7_SLP/sentence_type_histogram.png")
    

if __name__ == "__main__":
    task_1()
    task_2()
    task_3()