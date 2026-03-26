Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import random
... 
... category = input("Выберите категорию (работа, хобби, технологии): ")
... ideas = ideas_by_category.get(category, [])
... if ideas:
...     print("Вот ваша идея:", random.choice(ideas))
... else:
...     print("Категория не найдена.")
... ideas_by_category = {
...     'работа': ['Найти новую работу', 'Обучиться новой профессии'],
...     'хобби': ['Начать рисовать', 'Выучить гитару'],
...     'технологии': ['Изучить Python', 'Создать сайт']
