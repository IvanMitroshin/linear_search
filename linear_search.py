import random
import timeit

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
"""
Временная сложность O(n) зависит от размера списка, чем больше элементов, тем больше времени будет занимать поиск
Пространственная сложность O(1) используется фиксированный объем памяти и не требуется дополнительной
"""

arr_100 = [random.randint(1, 1000) for _ in range(100)]
print(f"Список из 100 чисел:",arr_100)

test_values = [arr_100[0], arr_100[49], arr_100[99]]

for target in test_values:
    result = linear_search(arr_100, target)
    if result != -1:
        print(f"Число {target} найдено")
    else:
        print(f"Число {target} не найдено")

arr_10 = [random.randint(1, 1000) for _ in range(10)]
arr_100 = [random.randint(1, 1000) for _ in range(100)]
arr_1000 = [random.randint(1, 1000) for _ in range(1000)]

target_10 = arr_10[5]
target_100 = arr_100[50]
target_1000 = arr_1000[500]

print(f"Время выполнения - 10 элеметов:",timeit.timeit(lambda: linear_search(arr_10, target_10), number=1000))
print(f"Время выполнения - 100 элеметов:",timeit.timeit(lambda: linear_search(arr_100, target_100), number=1000))
print(f"Время выполнения - 1000 элеметов:",timeit.timeit(lambda: linear_search(arr_1000, target_1000), number=1000))