try:
    height = int(input("Podaj wysokość prostokątu: "))
    width = int(input("Podaj szerokość prostokątu: "))

    for i in range(height):
        print("+" + "---+" * width)
        print(f"{'|':4}" * (width + 1))
    print("+" + "---+" * width)
except ValueError:
    print("Podano złe wymiary prostokątu")
