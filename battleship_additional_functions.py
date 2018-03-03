import random
from battleship_ship import Ship


def read_file(path):
    """
    Read data from file and store to 2D list
    :param path: path to the file
    :return: battlefield in format of 2D list
    """
    with open(path, 'r') as field_file:
        battlefield = [[ch for ch in row.strip('\n')] for row in field_file]
    return battlefield


def has_ship_general(bf, position):
    """
    Check if there is a ship on specified position
    :param bf: 2D list representation of a battlefield: list(list)
    :param position: Coordinates of a position on a battlefield: tuple
    :return: True if on that position is a ship, else False
    """
    if not (0 <= position[0] <= 9) or not (0 <= position[1] <= 9):
        return False
    return bool(bf[position[0]][position[1]])


# def has_ship(bf, position):
#     """
#     :param bf: 2D list representation of a battlefield: list(list)
#     :param position: Coordinates of a position on a battlefield: tuple
#     :return: True if on that position is an alive ship, else False
#     """
#     if not (1 <= position[1] <= 10) or not ('A' <= position[0] <= 'J'):
#         return False
#     x, y = position[1] - 1,  ord(position[0]) - 65
#     ship = bf[x][y]
#     # if there is no ship at all
#     if not ship:
#         return False
#     # if ship is drown
#     if


def ship_size(bf, position):
    """
    :param bf: 2D list representation of a battlefield: list(list)
    :param position: Coordinates of a position on a battlefield: tuple
    :return: length of ship, part of which is on that position: int
    """
    x, y = position[0], position[1]
    up, down, left, right = 0, 0, 0, 0
    while x - up - 1 >= 0 and bf[x - up - 1][y]:
        up += 1
    while x + down + 1 < 10 and bf[x + down + 1][y]:
        down += 1
    while y - left - 1 >= 0 and bf[x][y - left - 1]:
        left += 1
    while y + right + 1 < 10 and bf[x][y + right + 1]:
        right += 1
    return max(up + down, left + right) + 1


def is_valid(bf):
    """
    :param bf: 2D list representation of a battlefield: list(list)
    :return: if the field is valid
    """
    ship_by_length_number = {1: 0, 2: 0, 3: 0, 4: 0}
    for x in range(10):
        for y in range(10):
            if has_ship_general(bf, (x, y)):
                # check if there are no ships on diagonals
                if (has_ship_general(bf, (x - 1, y - 1)) or
                        has_ship_general(bf, (x - 1, y + 1)) or
                        has_ship_general(bf, (x + 1, y - 1)) or
                        has_ship_general(bf, (x + 1, y + 1))):
                    return False

                ship_by_length_number[ship_size(bf, (x, y))] += 1
    # check if number of ships is correct
    if ship_by_length_number != {1: 4, 2: 6, 3: 6, 4: 4}:
        return False
    return True


def field_to_str(bf):
    """
    :param bf: 2D list representation of a battlefield: list(list)
    :return: string representation of battlefield
    """
    bf_txt = [['■' if bf[i][j] else ' ' for i in range(10)] for j in range(10)]
    first_line = '   A B C D E F G H I J\n'
    return first_line + '\n'.join([' ' * (2 - len(str(x + 1))) + str(x + 1) +
                                   ' ' + ' '.join(bf_txt[x])
                                   for x in range(10)])


def generate_field():
    """
    Random generate field that is valid for a game
    :return: 2D list representation of a battlefield: list(list)
    """
    while True:
        bf = [[None for j in range(10)] for i in range(10)]
        try:
            # place 4-len
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            # 0 - up, 1 - down, 2 - right, 3 - left
            direction = random.randint(0, 3)
            if direction == 0:
                if x - 3 < 0:
                    raise IndexError
                bf[x][y] = bf[x - 1][y] = bf[x - 2][y] = bf[x - 3][y] \
                    = Ship((x - 3, y), False, 4)
            elif direction == 1:
                if x + 3 > 9:
                    raise IndexError
                bf[x][y] = bf[x + 1][y] = bf[x + 2][y] = bf[x + 3][y] \
                    = Ship((x, y), False, 4)
            elif direction == 2:
                if y + 3 > 9:
                    raise IndexError
                bf[x][y] = bf[x][y + 1] = bf[x][y + 2] = bf[x][y + 3] \
                    = Ship((x, y), True, 4)
            else:
                if y - 3 < 0:
                    raise IndexError
                bf[x][y] = bf[x][y - 1] = bf[x][y - 2] = bf[x][y - 3] \
                    = Ship((x, y - 3), True, 4)

            # place 3-len
            for i in range(2):
                # 0 - horizontal, 1 - vertical
                direction = random.randint(0, 1)
                if direction:
                    x = random.randint(1, 8)
                    y = random.randint(0, 9)
                    bf[x - 1][y] = bf[x + 1][y] = bf[x][y] \
                        = Ship((x - 1, y), False, 3)
                else:
                    x = random.randint(0, 9)
                    y = random.randint(1, 8)
                    bf[x][y - 1] = bf[x][y + 1] = bf[x][y] \
                        = Ship((x, y - 1), True, 3)

            # place 2-len
            for i in range(3):
                x = random.randint(0, 9)
                y = random.randint(0, 9)
                # 0 - up, 1 - down, 2 - right, 3 - left
                direction = random.randint(0, 3)
                if direction == 0:
                    if x - 1 < 0:
                        raise IndexError
                    bf[x][y] = bf[x - 1][y] = Ship((x - 1, y), False, 2)
                elif direction == 1:
                    if x + 1 > 9:
                        raise IndexError
                    bf[x][y] = bf[x + 1][y] = Ship((x, y), False, 2)
                elif direction == 2:
                    if y + 1 > 9:
                        raise IndexError
                    bf[x][y] = bf[x][y + 1] = Ship((x, y), True, 2)
                else:
                    if y - 1 < 0:
                        raise IndexError
                    bf[x][y] = bf[x][y - 1] = Ship((x, y - 1), True, 2)

            # place 1-len
            for i in range(4):
                x = random.randint(0, 9)
                y = random.randint(0, 9)
                bf[x][y] = Ship((x, y), True, 1)
            if is_valid(bf):
                break
        except (IndexError, KeyError):
            continue
    return bf
