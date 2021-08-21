n, k, x, y = input().split()  # ввод количества этажей и тп
floor = [[] for i in range(int(n))]  # массив с этажами(в каждом этаже комнаты)
q = int(input())  # количество запросов
a = input().split()[:q]  # ввод запросов
a = [int(el) for el in a]  # Перевод всех запросов в числа
how = 0  # общее количество комнат
while how < max(a):  # пока всего комнат в массиве floor меньше самого максимального запроса
    # далее идёт заполнение этажей как в условии задачи
    for g in range(1, int(n) + 1):
        if g % int(k) == 0:
            for i in range(1, int(x) + 1):
                floor[g - 1].append(how + i)
            how += int(x)
        else:
            for i in range(1, int(y) + 1):
                floor[g - 1].append(how + i)
            how += int(y)

for el_2 in a:  # перечесление запросов
    num = 0  # номер этажа
    for el in floor:  # перечесление этажей
        num += 1
        if el_2 in el:
            # если на этом этаже есть комната из запроса, то выводим номер этажа
            print(num)
