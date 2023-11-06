Раиль Галимов, [06.11.2023 9:03]
# class MusicAlbum:
#     def init(self, title, artist, release_year, genre, tracklist):
#         self.title = title
#         self.artist = artist
#         self.release_year = release_year
#         self.genre = genre
#         self.tracklist = tracklist
#
#     def get_info(self):
#         print(f'''
# Название: {self.title}
# Исполнитель: {self.artist}
# Год выпуска: {self.release_year}
# Жанр: {self.genre}
# Список треков: {self.tracklist}
#                 ''')
#     def play_random_track(self):
#         return random.choice(self.tracklist)
#
# album4 = MusicAlbum("Deutschland", "Rammstein", 2019, "Neue Deutsche Härte",
#                     ["Deutschland", "Radio", "Zeig dich", "Ausländer", "Sex",
#                      "Puppe", "Was ich liebe", "Diamant", "Weit weg", "Tattoo",
#                      "Hallomann"])
# album4.get_info()
# print(album4.play_random_track())

# class Student:
#
#     def init(self, name, age, grade, scores):
#         self.name = name
#         self.age = age
#         self.grade = grade
#         self.scores = scores
#
#     def info(self):
#         print('Имя', self.name)
#         print('Возраст', self.age)
#         print('Класс', self.grade)
#         print('Оценки', self.scores)
#
#     def average_score(self):
#         return sum(self.scores) / len(self.scores)
#
#
# student2 = Student("Егор Данилов", 12, "5B", [5, 4, 4, 5])
# student2.info()
# print(student2.average_score())

# class Recipe:
#     def init(self, name, ingredients):
#         self.name = name
#         self.ingredients = ingredients
#
#     def print_ingredients(self):
#         print(f"Ингредиенты для {self.name}")
#         for ingredient in self.ingredients:
#             print(f"- {ingredient}")
#
#     def cook(self):
#         print(f"Сегодня мы готовим {self.name}.")
#         print(f"Выполняем инструкцию по приготовлению блюда {self.name}...")
#         print(f"Блюдо {self.name} готово!")
#
# spaghetti = Recipe("Спагетти болоньезе", ["Спагетти", "Фарш", "Томатный соус", "Лук", "Чеснок", "Соль"])
# spaghetti.print_ingredients()
# spaghetti.cook()
# cake = Recipe("Кекс", ["Мука", "Яйца", "Молоко", "Сахар", "Сливочное масло", "Соль", "Ванилин"])
# cake.print_ingredients()
# cake.cook()

# class Publisher:
#     def init(self, name, location):
#         self.name = name
#         self.location = location
#
#     def get_info(self):
#         return f"{self.name} ({self.location})"
#
#     def publish(self, message):
#         print(f'Готовим "{message}" к публикации в {self.get_info()}')
#
#
# class BookPublisher(Publisher):
#     def init(self, name, location, num_authors):
#         super().init(name, location)
#         self.num_authors = num_authors
#
#     def publish(self, title, author):
#         print(f"Передаем рукопись '{title}', написанную автором {author} в издательство {self.get_info()}")
#
#
# class NewspaperPublisher(Publisher):
#     def init(self, name, location, num_pages):
#         super().init(name, location)
#         self.num_pages = num_pages
#
#     def publish(self, title):
#         print(f'Печатаем свежий номер со статьей "{title}" на главной странице в издательстве {self.get_info()}')
#
#
# publisher = Publisher("АБВГД Пресс", "Москва")
# publisher.publish("Справочник писателя")
#
# book_publisher = BookPublisher("Важные Книги", "Самара", 52)
# book_publisher.publish("Приключения Чебурашки", "В.И. Пупкин")
#
# newspaper_publisher = NewspaperPublisher("Московские вести", "Москва", 12)
# newspaper_publisher.publish("Новая версия Midjourney будет платной")

Раиль Галимов, [06.11.2023 9:03]
# class BankAccount:
#     def init(self, balance, interest_rate):
#         self.balance = balance
#         self.interest_rate = interest_rate
#         self.transactions = []
#
#     def deposit(self, amount):
#         self.balance += amount
#         self.transactions.append(f"Внесение наличных на счет: {amount}")
#
#     def withdraw(self, amount):
#         if self.balance >= amount:
#             self.balance -= amount
#             self.transactions.append(f'Снятие наличных: {amount}')
#         else:
#             print("Недостаточно средств на счете")
#
#     def add_interest(self):
#         sum_balance_interest = self.balance * self.interest_rate
#         self.balance += sum_balance_interest
#         self.transactions.append(f'Начислены проценты по вкладу {sum_balance_interest}')
#
#     def history(self):
#         for transaction in self.transactions:
#             print(transaction)
#
# # создаем объект счета с балансом 100000 и процентом по вкладу 0.05
# account = BankAccount(100000, 0.05)
#
# # вносим 15 тысяч на счет
# account.deposit(15000)
#
# # снимаем 7500 рублей
# account.withdraw(7500)
#
# # начисляем проценты по вкладу
# account.add_interest()
#
# # печатаем историю операций
# account.history()


# class Employee:
#     def init(self, name, age, salary):
#         self.name = name
#         self.age = age
#         self.salary = salary
#         self.bonus = 0
#
#     def get_name(self):
#         return self.name
#
#     def get_age(self):
#         return self.age
#
#     def get_salary(self):
#         return self.salary
#
#     def set_bonus(self, bonus):
#         self.bonus = bonus
#
#     def get_bonus(self):
#         return self.bonus
#
#     def get_total_salary(self):
#         return self.salary + self.bonus
#
#
# # создаем сотрудника с именем, возрастом и зарплатой
# employee = Employee("Марина Арефьева", 30, 90000)
#
# # устанавливаем бонус для сотрудника
# employee.set_bonus(15000)
#
# # выводим имя, возраст, зарплату, бонус и общую зарплату сотрудника
# print("Имя:", employee.get_name())
# print("Возраст:", employee.get_age())
# print("Зарплата:", employee.get_salary())
# print("Бонус:", employee.get_bonus())
# print("Итого начислено:", employee.get_total_salary())


# class Animal:
#     def init(self, name, species, legs):
#         self.name = name
#         self.species = species
#         self.legs = legs
#
#     def voice(self):
#         print(f"{self.name} подает голос")
#
#     def move(self):
#         print(f"{self.name} дергает хвостом")
#
# class Dog(Animal):
#     def init(self, name, breed, legs):
#         super().init(name, breed, legs)
#         self.breed = breed
#
#     def bark(self):
#         print(f"{self.breed} {self.name} лает")
#
# class Bird(Animal):
#     def init(self, name, species, wingspan):
#         super().init(name, species, 2)
#         self.wingspan = wingspan
#
#     def fly(self):
#         print(f"{self.species} {self.name} летaeт")
#
#
# dog = Dog("Геральт", "доберман", 4)
# bird = Bird("Вася", "попугай", 2)
# dog.voice()
# bird.voice()
# dog.move()
# bird.move()
# dog.bark()
# bird.fly()