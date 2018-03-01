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
        """
        x, y = coords
        self.__ships[x][y].shoot_at(coords)
        self.__ships[x][y] = 'X'

    def field_without_ships(self):
        """
        :return: string of field with marked cells that where hit by enemy
        """
        bf_txt = [['X' if self.__ships[i][j] == 'X'
                   else ' ' for i in range(10)] for j in range(10)]

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
                   else '■' if isinstance(self.__ships[i][j], Ship)
                   else ' ' for i in range(10)] for j in range(10)]

        first_line = '   A B C D E F G H I J\n'
        return first_line + '\n'.join([' ' * (2 - len(str(x + 1))) +
                                       str(x + 1) + ' ' + ' '.join(bf_txt[x])
                                       for x in range(10)])