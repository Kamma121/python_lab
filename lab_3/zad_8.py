# a) Znajdź listę elementów występujących jednocześnie w obu sekwencjach (bez powtórzeń)
first_list = [1, 2, 3, 4, 5, 9, 21, 1239, 100]
second_list = [1, 2, 3, 4, 22, 1238218, 1010]

intersection = list(set(first_list) & set(second_list))
print("Wszystkie elementy występujące w obu sekwencjach liczb bez powtórzeń: ")
print(intersection)

# b) Znajdź listę wszystkich elementów z obu sekwencji (bez powtórzeń).
union = list(set(first_list) | set(second_list))
print("Wszystkie elementy z obu sekwencji liczb bez powtórzeń: ")
print(union)
