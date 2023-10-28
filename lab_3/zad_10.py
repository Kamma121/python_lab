dictionary = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

# Druga możliwość stworzenia słownika
values = [('I', 1), ('V', 5), ('X', 10), ('L', 50), ('C', 100), ('D', 500), ('M', 1000)]
second_dictionary = dict(values)


def roman2int(roman_number):
    result = 0
    prev_value = 0
    for number in reversed(roman_number):
        value = dictionary[number]
        if value < prev_value:
            result -= value
        else:
            result += value
        prev_value = value
    return result


roman_input = str(input("Podaj liczbę w systemie rzymskim: "))
print(f"Liczba w systemie arabskim: {roman2int(roman_input)}")
