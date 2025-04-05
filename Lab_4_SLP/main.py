from func_lab4 import *

def main():
    output_dir = setup_directories()
     
    # Ініціалізація списків слів
    nouns = initialize_nouns()
    verbs = initialize_verbs()
    adjectives = initialize_adjectives()
    
    # Створення CSV-файлів
    create_csv_file(output_dir, "список_іменників.csv", nouns)
    create_csv_file(output_dir, "список_дієслів.csv", verbs)
    create_csv_file(output_dir, "список_прикметників.csv", adjectives)

    print("Всі файли успішно створені!")

    print("\nВипадкове речення:", random_sentence(nouns, verbs, adjectives))
    
    #завдання 2
    print(f"\nКількість символів у тексті \"Втеча з Шоушенка\" з пробіліми: {len_text_with_spaces()}")
    print(f"Кількість символів у тексті \"Втеча з Шоушенка\" без пробілів: {len_text_without_spaces()}")

    print(f"Кількість слів у тексті \"Втеча з Шоушенка\": {total_number_of_words()}")
    print(f"Загальна кількість слів без повторів у тексті \"Втеча з Шоушенка\": {total_number_of_different_words()}")

    print(f"Кількість слів які є унікальніми у тексті \"Втеча з Шоушенка\": {words_one()}")
    
    # завдання 3 варіант 5
    print(lists_of_emotions())

if __name__ == "__main__":
    main()