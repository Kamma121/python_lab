while True:
    user_input = input("Podaj liczbę lub wpisz 'stop' by zakończyć: ")

    if user_input == 'stop':
        break

    try:
        x = float(user_input)
        print(f"x = {x}, {x}^3 = {x ** 3}")
    except ValueError:
        print("To nie jest liczba rzeczywista. Spróbuj ponownie.")
