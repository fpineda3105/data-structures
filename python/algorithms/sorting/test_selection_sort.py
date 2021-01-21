def sort_by_selection(arr):
    for i in range(len(arr)):
        min_value = min(arr[i:])
        min_index = arr.index(min_value)
        if (i != min_index):
            arr[min_index] = arr[i]
            arr[i] = min_value

    return arr


# ------- Tests ----
def test_short_array_selection():
    arr = [5, 2, 4, 6, 7, 9, 1, 8, 3]
    assert sort_by_selection(arr) == [1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_medium_array_selection():
    arr = [8, 67, 2, 10, 61, 59, 100, 35, 76, 80, 45, 69]
    assert sort_by_selection(arr) == [2, 8, 10, 35, 45, 59, 61, 67, 69, 76, 80, 100]
