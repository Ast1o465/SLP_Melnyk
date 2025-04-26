class CityGame:
    def __init__(self):
        """
        Ініціалізація гри "Міста".
        Створює порожній список гравців, множину міст, словник країн та список географічних питань.
        """
        self.players = []
        self.cities = set()
        self.countries = {}
        self.geo_questions = []

    def register_player(self, player_name):
        """
        Реєстрація нового гравця.
        Якщо гравець з таким ім'ям вже зареєстрований, повертає False.
        Інакше додає гравця до списку та повертає True.
        """
        if player_name not in self.players:
            self.players.append(player_name)
            return True
        return False
    
    def all_players(self):
        """
        Повертає список усіх зареєстрованих гравців.
        """
        return self.players

    def add_city(self, city_name, country_name):
        """
        Додавання нового міста та країни.
        Якщо місто вже існує, нічого не робить.
        Якщо країна не існує, створює новий запис у словнику країн.
        Додає місто до множини міст та до списку міст країни.
        """
        self.cities.add(city_name)
        if country_name not in self.countries:
            self.countries[country_name] = []
        if city_name not in self.countries[country_name]:
            self.countries[country_name].append(city_name)

    def add_geo_question(self, question, answer):
        """
        Додавання географічного питання.
        Питання та відповідь зберігаються у вигляді словника у списку географічних питань.
        """
        self.geo_questions.append({'Питання': question, 'Відповідь': answer})

    def get_cities(self):
        """
        Повертає список усіх міст, які були додані до гри.
        """
        return list(self.cities)

    def get_countries(self):
        """
        Повертає список усіх країн, які були додані до гри.
        """
        return list(self.countries.keys())

    def get_geo_questions(self):
        """
        Повертає список усіх географічних питань, які були додані до гри.
        """
        return self.geo_questions

class Phone_book:
    def __init__(self):
        """
        Ініціалізація телефонної книги.
        Створює порожній словник для зберігання контактів.
        """
        self.contacts = {}

    def add_contact(self, name, phone_number):
        """
        Додавання нового контакту.
        Якщо контакт з таким ім'ям вже існує, нічого не робить.
        Інакше додає контакт до словника.
        """
        if name not in self.contacts:
            self.contacts[name] = phone_number
            return True
        return False

    def delete_contact(self, name):
        """
        Видалення контакту.
        Якщо контакт з таким ім'ям існує, видаляє його з словника.
        Інакше повертає False.
        """
        if name in self.contacts:
            del self.contacts[name]
            return True
        return False

    def edit_contact(self, name, new_name, new_phone_number):
        """
        Редагування контакту.
        Якщо контакт з таким ім'ям існує, змінює його ім'я та номер телефону.
        Інакше повертає False.
        """
        if name in self.contacts:
            del self.contacts[name]
            self.contacts[new_name] = new_phone_number
            return True
        return False

    def search_contact(self, name):
        """
        Пошук контакту за ім'ям.
        Якщо контакт з таким ім'ям існує, повертає його номер телефону.
        Інакше повертає None.
        """
        if name in self.contacts:
            return self.contacts[name]
        return None

    def get_all_contacts(self):
        """
        Повертає список усіх контактів у телефонній книзі.
        """
        return list(self.contacts.items())

    def call_number(self, name):
        """
        Виклик номера телефону контакту.
        Якщо контакт з таким ім'ям існує, повертає повідомлення про дзвінок.
        Інакше повертає повідомлення про те, що контакт не знайдено.
        """
        if name in self.contacts:
            return f"Дзвінок до {self.contacts[name]}..."
        return "Контакт не знайдено."

    def send_message(self, name, message):
        """
        Відправлення повідомлення контакту.
        Якщо контакт з таким ім'ям існує, повертає повідомлення про відправлення.
        Інакше повертає повідомлення про те, що контакт не знайдено.
        """
        if name in self.contacts:
            return f"Відправлення повідомлення на {self.contacts[name]}: {message}"
        return "Контакт не знайдено."
    
