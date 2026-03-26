import random

# Основной словарь идей
ideas_by_category = {
    'работа': ['Найти новую работу', 'Обучиться новой профессии'],
    'хобби': ['Начать рисовать', 'Выучить гитару'],
    'технологии': ['Изучить Python', 'Создать сайт']
}

# Взаимодействие с пользователем
category = input("Выберите категорию (работа, хобби, технологии): ")
ideas = ideas_by_category.get(category, [])
if ideas:
    print("Вот ваша идея:", random.choice(ideas))
else:
    print("Категория не найдена.")

# Функция для сохранения идеи
def save_favorite(idea):
    with open("favorites.txt", "a", encoding="utf-8") as file:
        file.write(idea + "\n")
    print("Идея сохранена в favorites.txt")
