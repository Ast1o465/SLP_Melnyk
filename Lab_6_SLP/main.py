import requests
from bs4 import BeautifulSoup
from collections import Counter
import re

def fetch_html(url):
    """Завантажує HTML-код сторінки за вказаним URL."""
    try:
        response = requests.get(url)  # Виконуємо HTTP-запит до сайту
        response.raise_for_status()   # Перевіряємо наявність помилок HTTP
        return response.text          # Повертаємо HTML-код сторінки
    except Exception as e:
        print(f"Помилка при завантаженні сторінки: {e}")
        return None

def extract_text(html_content):
    """Витягує текст з HTML-коду, ігноруючи теги."""
    soup = BeautifulSoup(html_content, "html.parser")  # Парсимо HTML
    # Витягуємо текст лише з тегу body
    text = soup.body.get_text(separator=' ', strip=True)
    return text

def count_word_frequency(text):
    """Підраховує частоту слів у тексті, ігноруючи слова менші за 3 символи."""
    # Видаляємо все, крім букв, і переводимо в нижній регістр
    words = [word for word in text.lower().split() if word.isalpha() and len(word) >= 3]
    return Counter(words)  # Повертаємо словник з частотою слів

def count_html_tags(html_content):
    """Підраховує частоту HTML-тегів у коді."""
    soup = BeautifulSoup(html_content, "html.parser")  # Парсимо HTML
    tags = [tag.name for tag in soup.find_all()]       # Збираємо всі імена тегів
    return Counter(tags)                               # Повертаємо частоту тегів

def count_links(html_content):
    """Підраховує кількість посилань (тег <a>) у HTML-коді."""
    soup = BeautifulSoup(html_content, "html.parser")  # Парсимо HTML
    return len(soup.find_all('a'))                     # Рахуємо кількість <a>

def count_images(html_content):
    """Підраховує кількість зображень (тег <img>) у HTML-коді."""
    soup = BeautifulSoup(html_content, "html.parser")  # Парсимо HTML
    return len(soup.find_all('img'))                   # Рахуємо кількість <img>

def write_to_file(filename, data):
    """Записує дані у файл."""
    with open(filename, 'w', encoding='utf-8') as file:
        for item in data:
            file.write(f"{item}\n")  # Записуємо кожен елемент у новий рядок

def main():
    """Основна функція програми."""
    url = input("Введіть URL сайту новин: ")  # Запитуємо URL у користувача
    
    html_content = fetch_html(url)            # Завантажуємо HTML-код сторінки
    if html_content:
        text = extract_text(html_content)     # Витягуємо текст зі сторінки
        word_frequency = count_word_frequency(text)  # Підраховуємо частоту слів
        tag_frequency = count_html_tags(html_content)  # Підраховуємо частоту тегів
        link_count = count_links(html_content)         # Рахуємо кількість посилань
        image_count = count_images(html_content)       # Рахуємо кількість зображень

        print("Частота слів:")
        for word, count in word_frequency.most_common(10):  # Виводимо 10 найчастіших слів
            print(f"{word}: {count}")

        print("\nЧастота HTML-тегів:")
        for tag, count in tag_frequency.items():            # Виводимо частоту тегів
            print(f"{tag}: {count}")

        print(f"\nКількість посилань (тег <a>): {link_count}")
        print(f"Кількість зображень (тег <img>): {image_count}") 

        # Запис результатів у файли
        write_to_file("Lab_6_SLP/word_frequency.txt", [f"{word}: {count}" for word, count in word_frequency.most_common()])
        write_to_file("Lab_6_SLP/tag_frequency.txt", [f"{tag}: {count}" for tag, count in tag_frequency.items()])
        write_to_file("Lab_6_SLP/links_and_images.txt", [f"Кількість посилань: {link_count}", f"Кількість зображень: {image_count}"])
    else:
        print("Не вдалося завантажити HTML-код сторінки.")

if __name__ == "__main__":
    main()