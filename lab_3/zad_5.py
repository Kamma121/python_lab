try:
    frame_length = int(input("Podaj długość miarki: "))

    frame = "|"
    numbers = "0"

    for i in range(frame_length):
        frame += "....|"
        numbers += f"{i + 1:5}"

    print(frame)
    print(numbers)
except ValueError:
    print("Podano złą długość miarki.")
