from alg import format_fast_sort

arr = []
try:
    print("Введите значения массива через запятую:")
    arr = list(map(int, input().split(",")))
except ValueError:
    print("Вводите только числа")

format_fast_sort(arr)
