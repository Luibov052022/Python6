# Задача 43: Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.

my_list = [int(input('Введите число: ')) for i in range (int(input('Сколько чисел собираетесь ввести? ')))]
new_list = [i for i in my_list if (my_list.count(i) == 1)]
print(f'{my_list} => {new_list}')