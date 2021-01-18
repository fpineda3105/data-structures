import random

def quick_sort(unordered_list):
    size = len(unordered_list)
    if (size < 2):
        return unordered_list
    
    pivotIndex = random.randrange(0, size)
    pivot = unordered_list[pivotIndex]
    
    minor_list = []
    major_list = []
    
    for i, val in enumerate(unordered_list):
        if (i != pivotIndex and val < pivot):
            minor_list.append(val)
            continue
        if (i != pivotIndex and val >= pivot):
            major_list.append(val)
                        
    return quick_sort(minor_list) + [pivot] + quick_sort(major_list)


# ----------- Tests -----------
def test_short_list():
    unordered_list = [5, 8, 12, 67, 43, 56, 9]
    assert quick_sort(unordered_list) == [5, 8, 9, 12, 43, 56, 67]
    
def test_medium_list():
    unordered_list = [5, 45, 100, 8, 12, 56, 99, 3, 67, 80, 43, 56, 9, 140]
    assert quick_sort(unordered_list) == [3, 5, 8, 9, 12, 43, 45, 56, 56, 67, 80, 99, 100, 140]


