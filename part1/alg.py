# Реализует сортировку подмассива
def partition(arr: [], start, last):
    i = start - 1
    j = last + 1
    index = arr[(start + (last - start) // 2)]
    while True:
        i += 1
        while arr[i] < index:
            i += 1
        j -= 1
        while arr[j] > index:
            j -= 1
        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]

# Реализует алгоритм сортировки
def my_quicksort(arr: [], left: int, right: int):
    if left < right:
        partition_index: int = partition(arr, left, right)
        my_quicksort(arr, left, partition_index)
        my_quicksort(arr, partition_index + 1, right)
    return arr




# Возвращает четные элементы массива
def check_even(arr: list[int]):
    even = []
    for i in arr:
        if i % 2 == 0:
            even.append(i)
    return even

# Сортирует массив методом быстрой сортировки. Возвращает отсортированный массив, список четных чисел, максимальное и минимальное значение в формате tuple
def fast_sort(arr: []) -> (list[int], list[int], (int, int)):
    if not arr:
        return [], [], ()
    arr = my_quicksort(arr, 0, len(arr) - 1)
    even = check_even(arr)
    return arr, even, (arr[0], arr[len(arr) - 1])

# Форматированный вывод
def format_fast_sort(arr: list[int]):
    sorted_arr, even, (min_value, max_value) = fast_sort(arr)
    print(f"Четные числа: {even}")
    print(f"Максимальное число: {max_value}")
    print(f"Минимальное число: {min_value}")
    print(f"Отсортированный список: {sorted_arr}")