from insertion_sort import insertion_sort


def test_insertion_sort():
    arr0 = [5, 2, 9, 1, 5, 6]
    assert insertion_sort(arr0) == sorted(arr0)

    arr1 = [5, 4, 7, 8, 3, 10, 1]
    assert insertion_sort(arr1) == sorted(arr1)

    arr2 = [6, 3, 100, 8, 1]
    assert insertion_sort(arr2) == sorted(arr2)
