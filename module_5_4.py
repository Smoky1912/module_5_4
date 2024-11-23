from module_5_3 import *

class House:
    houses_history = []  # атрибут класса для хран-я  ист-и строит-ва

    def __new__(cls, *args, **kwargs): # вызывается перед созд-ем нов. объекта
        instance = super(House, cls).__new__(cls) # создаем новый объект
        if args:   # доб-им назв. объекта в историю
            cls.houses_history.append(args[0]) # args[0] - первый эл-нт args
        return instance

    def __init__(self, name, number_of_floors): # определим метод __init__ с названием и кол-вом этажей
        # присвоим атрибутам названия и кол-ва этажей атрибуты
        self.name = name
        self.number_of_floors = number_of_floors

    def __del__(self): # перед удалением объекта выведем инф-цию
        print(f"{self.name} снесён, но он останется в истории")


# Пример:
home1 = House('ЖК Лазурные небеса', 37)
print(House.houses_history)  # ['ЖК Лазурные небеса']

home2 = House('ЖК АртСити', 10)
print(House.houses_history)  # ['ЖК Лазурные небеса', 'ЖК АртСити']

home3 = House('ЖК Весна', 18)
print(House.houses_history)  # ['ЖК Лазурные небеса', 'ЖК АртСити', 'ЖК Весна']

# Удаление
del home2
del home3

print(House.houses_history)  # ['ЖК Лазурные небеса', 'ЖК АртСити', 'ЖК Весна']
del home1