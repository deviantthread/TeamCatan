import sys
import random

# base
base_hexes = {
    "wd": 4,
    "sh": 4,
    "wh": 4,
    "br": 3,
    "or": 3,
    "de": 1
}

base_numbers = {
    "02": 1,
    "03": 2,
    "04": 2,
    "05": 2,
    "06": 2,
    "08": 2,
    "09": 2,
    "10": 2,
    "11": 2,
    "12": 1,
    "de": 1
}


def add_standard_expansion(hexes, numbers):
    hexes["wd"] = hexes.get("wd") + 2
    hexes["sh"] = hexes.get("sh") + 2
    hexes["wh"] = hexes.get("wh") + 2
    hexes["br"] = hexes.get("br") + 2
    hexes["or"] = hexes.get("or") + 2
    hexes["de"] = hexes.get("de") + 1

    numbers["02"] = 2
    numbers["03"] = 3
    numbers["04"] = 3
    numbers["05"] = 3
    numbers["06"] = 3
    numbers["08"] = 3
    numbers["09"] = 3
    numbers["10"] = 3
    numbers["11"] = 3
    numbers["12"] = 2
    numbers["de"] = 2

    return hexes, numbers


def add_special_expansion(hexes, numbers):
    hexes["wd"] = hexes.get("wd") + 2
    hexes["sh"] = hexes.get("sh") + 1
    hexes["wh"] = hexes.get("wh") + 1
    hexes["br"] = hexes.get("br") + 1
    hexes["or"] = hexes.get("or") + 1
    hexes["de"] = hexes.get("de") + 1

    numbers["02"] = 2
    numbers["03"] = 4
    numbers["04"] = 4
    numbers["05"] = 4
    numbers["06"] = 3
    numbers["08"] = 3
    numbers["09"] = 4
    numbers["10"] = 4
    numbers["11"] = 4
    numbers["12"] = 2
    numbers["de"] = 3

    return hexes, numbers


def generate_hexes(size):
    global base_hexes
    global base_numbers
    hexes = base_hexes
    layout = []
    numbers = base_numbers
    if size >= 4:
        hexes, numbers = add_standard_expansion(hexes, numbers)
        layout = [4, 5, 6, 6, 5, 4]
    if size >= 6:
        hexes, numbers = add_special_expansion(hexes, numbers)
        layout = [4, 5, 6, 7, 6, 5, 4]

    if not sum(layout) == sum(hexes.values()) == sum(numbers.values()):
        raise ArithmeticError("layout ({}), hexes ({}), numbers ({}) mismatch".format(sum(layout), sum(hexes.values()),
                                                                                      sum(numbers.values())))
    del numbers["de"]

    return hexes, numbers, layout


def print_board(hexes, numbers, layout):
    flat_hexes = []
    for hex, amount in hexes.items():
        for i in range(amount):
            flat_hexes.append(hex)

    flat_numbers = []
    for num, amount in numbers.items():
        for i in range(amount):
            flat_numbers.append(num)

    random.shuffle(flat_hexes)
    random.shuffle(flat_numbers)

    for row_size in layout:
        row_str = ""
        for i in range(row_size):
            hex = flat_hexes.pop()
            num = flat_numbers.pop() if hex != "de" else "00"
            row_str += num + hex + " "
        print(row_str.strip().center(50))


if __name__ == "__main__":
    if len(sys.argv) < 2 or int(sys.argv[1]) not in [4, 6]:
        print("need a size of value [4, 6]")
    else:
        hexes, numbers, layout = generate_hexes(int(sys.argv[1]))
        print_board(hexes, numbers, layout)
