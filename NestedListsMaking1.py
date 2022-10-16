# Способ 1. Создадим пустой список, потом n раз добавим в него новый элемент – список длины m, составленный из нулей:

n, m = int(input()), int(input())    # считываем значения n и m
my_list = []

for _ in range(n):
    my_list.append([0] * m)

print(my_list)