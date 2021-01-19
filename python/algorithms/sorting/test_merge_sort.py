def merge(left, right):
    i = 0
    j = 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i +=1
        else:
            result.append(right[j])
            j += 1
    
    if i < len(left):
        result.extend(left[i:])
    if j < len(right):
        result.extend(right[j:])
    
    return result


def merge_sort(elements):
    if (len(elements) == 1):
        return elements

    mid = len(elements) // 2
    left = elements[:mid]
    right = elements[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


# ----------- Tests -----------
def test_short_list():
    unordered_list = [5, 8, 12, 67, 43, 56, 9]
    assert merge_sort(unordered_list) == [5, 8, 9, 12, 43, 56, 67]


def test_medium_list():
    unordered_list = [5, 45, 100, 8, 12, 56, 99, 3, 67, 80, 43, 56, 9, 140]
    assert merge_sort(unordered_list) == [
        3, 5, 8, 9, 12, 43, 45, 56, 56, 67, 80, 99, 100, 140]
