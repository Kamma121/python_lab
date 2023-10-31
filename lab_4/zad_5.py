def odwracanie(L, left, right):
    if left < 0 or right < 0 or left >= len(L) or right >= len(L):
        return L
    while left < right:
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1


numbers = [1, 2, 3, 4, 5, 6]
odwracanie(numbers, 0, 4)
print(numbers)
