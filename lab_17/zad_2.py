def binarne_rek(L, left, right, y):
    """Wyszukiwanie binarne w wersji rekurencyjnej."""
    if left <= right:
        mid = left + (right - left) // 2
        if L[mid] == y:
            return mid
        elif L[mid] > y:
            return binarne_rek(L, left, mid - 1, y)
        else:
            return binarne_rek(L, mid + 1, right, y)
    else:
        return -1


def test_binarne_rek():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 20, 48, 123]
    right = len(numbers) - 1
    assert binarne_rek(numbers, 0, right, 2) == 1
    assert binarne_rek(numbers, 0, right, 6) == 5
    assert binarne_rek(numbers, 0, right, 12) == 9
    assert binarne_rek(numbers, 0, right, 48) == 11
    assert binarne_rek(numbers, 0, right, 315) == -1


test_binarne_rek()
