def make_ruler(n):
    frame = "|"
    numbers = "0"

    for i in range(n):
        frame += "....|"
        numbers += f"{i + 1:5}"
    return f"{frame}\n{numbers}"


print(make_ruler(12))
print("\n\n")


def make_grid(rows, cols):
    try:
        rows = int(rows)
        cols = int(cols)
        grid = ""
        for i in range(rows):
            grid += "+" + "---+" * cols + "\n"
            grid += f"{'|':4}" * (cols + 1) + "\n"
        grid += "+" + "---+" * cols
        return grid
    except ValueError:
        return "Podano złe wymiary siatki"


print(make_grid(2, 4))
