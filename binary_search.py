import random
import timeit
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
"""
Временная сложность O(log n) обеспечивает быстрый поиск благодаря сортировке и разделению списка пополам
Пространственная сложность O(1) используется фиксированный объем памяти и не требуется дополнительной
"""

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

arr_100 = sorted(random.randint(1, 1000) for _ in range(100))
print(f"Список из 100 чисел:", arr_100)

test_values = [arr_100[0], arr_100[49], arr_100[99]]

for target in test_values:
    result = binary_search(arr_100, target)
    if result != -1:
        print(f"Число {target} найдено")
    else:
        print(f"Число {target} не найдено")

target_100 = arr_100[50]

print(f"Бинарный поиск: 100 элементов, время выполнения -", timeit.timeit(lambda: binary_search(arr_100, target_100), number=1000))
print(f"Линейный поиск: 100 элементов, время выполнения -", timeit.timeit(lambda: linear_search(arr_100, target_100), number=1000))
