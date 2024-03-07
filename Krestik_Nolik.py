def welcome():
    print("  --------------------")
    print("  --------Добро-------")
    print("  -----пожаловать!!!--")
    print("  -------В игру-------")
    print("  --Крестики - Нолики-")
    print("  --------------------")
    print("  ----Формат ввода:---")
    print("  -x - номер строки---")
    print("  -y - номер стоблика-")


def demonstrate():
    print()
    print("    | x |             ")
    print("----------------------")
    print("| y |   | 0 | 1 | 2 | ")
    print("----------------------")
    for number, line in enumerate(field):
        print(f"    | {number} | {' | '.join(line)} | ")
        print("    ------------------")


def entry():
    print(f"Ваш ход:")
    while True:
        x, y = input("x = "), input("y = ")
        if not (x.isdigit()) or not (y.isdigit()):
            print("Введите целые числа!")
            continue
        x, y = int(x), int(y)
        if 0 > x or x > 2 or 0 > y or y > 2:
            print("Координаты вне  диапазона!")
            continue
        if field[x][y] != " ":
            print("Клетка уже занята!")
            continue
        return x, y


def win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграли крестики!!!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграли нолики!!!")
            return True
    return False


welcome()
field = [[" "] * 3 for i in range(3)]
lot = 0
while True:
    lot += 1
    demonstrate()
    if lot % 2 == 0:
        print("Очередь нолика!")
    else:
        print("Очередь крестика!")

    x, y = entry()

    if lot % 2 == 0:
        field[x][y] = "0"
    else:
        field[x][y] = "X"

    if win():
        break

    if lot == 9:
        print("--------")
        print(" Ничья! ")
        print("--------")
        break
