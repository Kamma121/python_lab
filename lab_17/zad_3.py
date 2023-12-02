def mediana_sort(L, left, right):
    """Znajdowanie mediany przez posortowanie."""
    L.sort()
    mid = (left + right) // 2
    return L[mid]


def test_mediana_sort():
    numbers = [5, 8, -1, 6, 6, 1, 10]
    right = len(numbers)
    assert mediana_sort(numbers, 0, right) == 6


test_mediana_sort()
