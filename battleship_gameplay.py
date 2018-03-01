from battleship_additional_functions import generate_field
from battleship_ship import Ship
import re
import random


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
        if self.__ships[x][y]:
            self.__ships[x][y].shoot_at(coords)
            self.__ships[x][y] = 'X'
        else:
            self.__ships[x][y] = '•'

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


class Player:

    def __init__(self, name):
        """
        Create Player object
        :param name: name of the player
        """
        self.__name = name

    def read_position(self, number):
        """
        Read from keyboard players's next hit
        :number: number of player to display for input field
        :return: Coordinate, where player wants to hit
        """
        while True:
            move = input('Player {}, enter move: '.format(number + 1))
            if re.match(r'^[A-J][1-9]|10$', move):
                return int(move[1]) - 1, ord(move[0]) - 65
            else:
                print('Wrong format!!! Try again!')


class Game:

    def __init__(self):
        """
        Initialize new game
        """
        print('Game Battlefield')
        self.__players = [Player(input('Player 1 name: ')),
                          Player(input('Player 2 name: '))]
        self.__fields = [Field(), Field()]
        self.__current_player = random.randint(0, 1)

    def make_move(self):
        """
        Read coordinates of hit of player and make a hit
        :return: coordinates of hit of player
        """
        coords = self.__players[self.__current_player].\
            read_position(self.__current_player)
        self.__fields[self.__current_player ^ 1].shoot_at(coords)
        # change current player
        self.__current_player ^= 1

    def field_without_ships(self, index):
        """
        :param index: index of player, whose field to return
        :return: string representation of field without ships(str)
        """
        return ('Field of player {}:\n'.format(index + 1) +
                self.__fields[index].field_without_ships())

    def field_with_ships(self, index):
        """
        :param index: index of player, whose field to return
        :return: string representation of field with ships(str)
        """
        return ('Field of player {}:\n'.format(index + 1) +
                self.__fields[index].field_with_ships())


if __name__ == '__main__':
    # start the game
    game = Game()
    print(game.field_with_ships(0))
    print(game.field_with_ships(1))
    game.make_move()
    print(game.field_with_ships(0))
    print(game.field_with_ships(1))
