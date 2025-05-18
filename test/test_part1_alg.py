from part1.alg import fast_sort


def test_zero_len_arr():
    """Тестируем функцию fast_sort с пустым массивом."""
    arr = []
    arr, even, min_max = fast_sort(arr)
    assert arr == []
    assert even == []
    assert min_max == ()


def test_one_len_arr():
    """Тестируем функцию fast_sort с массивом длиной 1."""
    arr = [1]
    arr, even, min_max = fast_sort(arr)
    assert arr == [1]
    assert even == []
    assert min_max == (1, 1)


def test_two_len_arr():
    """Тестируем функцию fast_sort с массивом длиной 2."""
    arr = [1, 2]
    arr, even, min_max = fast_sort(arr)
    assert arr == [1, 2]
    assert even == [2]
    assert min_max == (1, 2)


def test_equals_arr():
    """Тестируем функцию fast_sort с массивом, содержащим одинаковые элементы."""
    arr = [1, 1, 1, 1, 1, 1]
    arr, even, min_max = fast_sort(arr)
    assert arr == [1, 1, 1, 1, 1, 1]
    assert even == []
    assert min_max == (1, 1)


def test_not_equals_arr():
    """Тестируем функцию fast_sort с массивом, содержащим разные элементы."""
    arr = [1, 3, 12, 5, 32, 8]
    arr, even, min_max = fast_sort(arr)
    assert arr == [1, 3, 5, 8, 12, 32]
    assert even == [8, 12, 32]
    assert min_max == (1, 32)


def test_equals_and_not_equals_arr():
    """Тестируем функцию fast_sort с массивом,
    содержащим как одинаковые, так и разные элементы."""
    arr = [1, 3, 1, 5, 2, 8]
    arr, even, min_max = fast_sort(arr)
    assert arr == [1, 1, 2, 3, 5, 8]
    assert even == [2, 8]
    assert min_max == (1, 8)


def test_task_example():
    """Тестируем функцию fast_sort с примером из задания."""
    arr = [1, 3, 4, 7, 8, 10]
    arr, even, min_max = fast_sort(arr)
    assert arr == [1, 3, 4, 7, 8, 10]
    assert even == [4, 8, 10]
    assert min_max == (1, 10)
