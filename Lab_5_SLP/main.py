from class_lab import CityGame, Phone_book

def main():
    city_game = CityGame()
    phone_book = Phone_book()

    while True:
        print("Оберіть опцію:")
        print("1. Гра 'Міста'")
        print("2. Телефонна книга")
        print("0. Вийти")
        choice = input("Ваш вибір: ")

        if choice == "1":
            while True:
                print("\nФункції гри 'Міста':")
                print("1. Реєстрація нового гравця")
                print("2. Всі гравці")
                print("3. Додати географічне питання")
                print("4. Показати всі географічні питання")
                print("5. Додати місто")
                print("6. Показати всі країни")
                print("7. Показати всі міста")
                print("0. Вийти")

                sub_choice = input("Ваш вибір: ")
                if sub_choice == "1":
                    player_name = input("Введіть ім'я гравця: ")
                    if player_name not in city_game.all_players():
                        city_game.register_player(player_name)
                        print(f"Гравець {player_name} успішно зареєстрований.")
                    else:
                        print(f"Гравець {player_name} вже зареєстрований.")

                elif sub_choice == "2":
                    print("Гравці:", list(city_game.all_players()))

                elif sub_choice == "3":
                    question = input("Введіть питання: ")
                    answer = input("Введіть відповідь: ")
                    city_game.add_geo_question(question, answer)
                    print(f"Географічне питання '{question}' з відповіддю '{answer}' додано.")

                elif sub_choice == "4":
                    print("Географічні питання:", city_game.get_geo_questions())

                elif sub_choice == "5":
                    city_name = input("Введіть назву міста: ")
                    country_name = input("Введіть назву країни: ")
                    city_game.add_city(city_name, country_name)
                    print(f"Місто '{city_name}' в країні '{country_name}' додано.")
                elif sub_choice == "6":
                    print("Країни:", city_game.get_countries())
                    
                elif sub_choice == "7":
                    print("Міста:", city_game.get_cities())

                elif sub_choice == "0":
                    print("Вихід з гри 'Міста'.")
                    break
                else:
                    print("Невірний вибір. Спробуйте ще раз.")

                

        elif choice == "2":
            while True:
                print("\nФункції телефонної книги:")
                print("1. Додати контакт")
                print("2. Видалити контакт")
                print("3. Редагувати контакт")
                print("4. Показати всі контакти")
                print("5. Пошук контакту")
                print("6. Позвонити контакту")
                print("7. Відправити повідомлення контакту")
                print("0. Вийти")

                sub_choice = input("Ваш вибір: ")

                if sub_choice == "1":
                    name = input("Введіть ім'я: ")
                    phone = input("Введіть номер телефону: ")
                    if name in phone_book.contacts:
                        print(f"Контакт {name} вже існує.")
                    else:
                        print(f"Контакт {name} додано.")
                        phone_book.add_contact(name, phone)

                elif sub_choice == "2":
                    name = input("Введіть ім'я контакту для видалення: ")
                    if name in phone_book.contacts:
                        phone_book.delete_contact(name)
                        print(f"Контакт {name} видалено.")
                    else:
                        print(f"Контакт {name} не знайдено.")
                        
                elif sub_choice == "3":
                    name = input("Введіть ім'я контакту для редагування: ")
                    new_name = input("Введіть нове ім'я: ")
                    new_phone = input("Введіть новий номер телефону: ")
                    
                    if name in phone_book.contacts:
                        phone_book.edit_contact(name, new_name, new_phone)
                        print(f"Контакт {name} відредаговано на {new_name} з номером {new_phone}.")
                    else:
                        print(f"Контакт {name} не знайдено.")

                elif sub_choice == "4":
                    print("Контакти:", phone_book.get_all_contacts())

                elif sub_choice == "5":
                    name = input("Введіть ім'я для пошуку: ")
                    contact = phone_book.search_contact(name)
                    print("Контакт:", contact)
                    
                elif sub_choice == "6":
                    name = input("Введіть ім'я контакту для дзвінка: ")
                    if name in phone_book.contacts:
                        phone_book.call_number(name)
                        print(f"Дзвоню {name} на номер {phone_book.contacts[name]}...")
                    else:
                        print(f"Контакт {name} не знайдено.")

                elif sub_choice == "7":
                    name = input("Введіть ім'я контакту для відправлення повідомлення: ")
                    message = input("Введіть повідомлення: ")
                    if name in phone_book.contacts:
                        print(f"Відправляю повідомлення {message} на номер {phone_book.contacts[name]}...")
                    else:
                        print(f"Контакт {name} не знайдено.")
                    phone_book.send_message(name, message)

                elif sub_choice == "0":
                    print("Вихід з телефонної книги.")
                    break
                else:
                    print("Невірний вибір. Спробуйте ще раз.")  
        elif choice == "0":
            print("Вихід з програми.")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()