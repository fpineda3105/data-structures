def binary_search(arr, elem):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = low + high // 2
        guest = arr[mid]
        if (guest == elem):
            return mid
        if (guest > elem):
            high = mid - 1
        else:
            low = mid + 1
    return None

# ------- Tests ----
def test_binary_search():
    array = [1, 3, 5, 7, 9, 10, 11]
    assert binary_search(array, 7) == 3


def test_binary_search_none():
    array = [10, 33, 54, 77, 92, 104, 115, 160]
    assert binary_search(array, 7) == None



