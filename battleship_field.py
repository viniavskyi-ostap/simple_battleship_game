from battleship_additional_functions import generate_field
from battleship_ship import Ship


class Field:

    def __init__(self):
        """
        Create object of class Field
        """
        self.__ships = generate_field()

    def shoot_at(self, coords):
        """
        Mark cell with given coordinates as killed
        :param coords: coordinates of the hit
        :return: if that field shout be attacked again
        """
        hit_again = False
        x, y = coords
        if isinstance(self.__ships[x][y], Ship):
            self.__ships[x][y].shoot_at(coords)
            hit_again = True
            # mark area around dead ship
            if self.__ships[x][y].is_destroyed():
                corpse = self.__ships[x][y]
                x1, y1 = corpse.bow
                if corpse.horizontal:
                    for i in range(-1, corpse.length() + 1):
                        if 1 <= x1 and 0 <= y1 + i <= 9:
                            self.__ships[x1 - 1][y1 + i] = '•'
                        if x1 <= 8 and 0 <= y1 + i <= 9:
                            self.__ships[x1 + 1][y1 + i] = '•'
                    if 1 <= y1:
                        self.__ships[x1][y1 - 1] = '•'
                    if y1 + corpse.length() <= 9:
                        self.__ships[x1][y1 + corpse.length()] = '•'
                else:
                    for i in range(-1, corpse.length() + 1):
                        if 1 <= y1 and 0 <= x1 + i <= 9:
                            self.__ships[x1 + i][y1 - 1] = '•'
                        if y1 <= 8 and 0 <= x1 + i <= 9:
                            self.__ships[x1 + i][y1 + 1] = '•'
                    if 1 <= x1:
                        self.__ships[x1 - 1][y1] = '•'
                    if x1 + corpse.length() <= 9:
                        self.__ships[x1 + corpse.length()][y1] = '•'

            self.__ships[x][y] = 'X'
        else:
            self.__ships[x][y] = '•'
        return hit_again

    def field_without_ships(self):
        """
        :return: string of field with marked cells that where hit by enemy
        """
        bf_txt = [['X' if self.__ships[i][j] == 'X'
                   else '•' if self.__ships[i][j] == '•'
                   else ' ' for j in range(10)] for i in range(10)]

        first_line = '   A B C D E F G H I J\n'
        return first_line + '\n'.join([' ' * (2 - len(str(x + 1))) +
                                       str(x + 1) + ' ' + ' '.join(bf_txt[x])
                                       for x in range(10)])

    def field_with_ships(self):
        """
        :return: string of field with marked cells that where hit by enemy
        and ships
        """
        bf_txt = [['X' if self.__ships[i][j] == 'X'
                   else '•' if self.__ships[i][j] == '•'
                   else '■' if isinstance(self.__ships[i][j], Ship)
                   else ' ' for j in range(10)] for i in range(10)]

        first_line = '   A B C D E F G H I J\n'
        return first_line + '\n'.join([' ' * (2 - len(str(x + 1))) +
                                       str(x + 1) + ' ' + ' '.join(bf_txt[x])
                                       for x in range(10)])

    def is_destroyed(self):
        """
        Check if field is destroyed
        :return: if field is destroyed (bool)
        """
        for row in self.__ships:
            for cell in row:
                if isinstance(cell, Ship):
                    return False
        return True
