year = int(input())
animals = ["Крыса", "Корова", "Тигр", "Заяц", "Дракон", "Змея",
           "Лошадь", "Овца", "Обезьяна", "Петух", "Собака", "Свинья"]
colors = ["Зеленый", "Красный", "Желтый", "Белый", "Черный"]
start_year = 1984
cycle_position = (year - start_year) % 60
animal_index = cycle_position % 12
color_index = (cycle_position // 2) % 5
print(f"{animals[animal_index]}, {colors[color_index]}")