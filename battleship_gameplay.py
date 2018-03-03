from battleship_additional_functions import generate_field
from battleship_ship import Ship
import re
import random
import os


def clear_console():
    """
    Clear console in any OS
    """
    os.system('cls' if os.name == 'nt' else 'clear')


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
                return int(move[1:]) - 1, ord(move[0]) - 65
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
        # print field without ships of enemy of current player
        print(self.field_without_ships(self.__current_player ^ 1))
        # read coordinates
        coords = self.__players[self.__current_player].\
            read_position(self.__current_player)
        hit_again = self.__fields[self.__current_player ^ 1].shoot_at(coords)
        # change current player
        if not hit_again:
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

    def is_winner(self):
        """
        Check if game has winner
        :return: winner of the game(0 for 1st player and 1 for 2nd player)
                 or False if game is not over
        """
        for field in self.__fields:
            if field.is_destroyed():
                return self.__fields.index(field) ^ 1
        return False

    def play(self):
        """
        Gameplay of the game
        """
        while True:
            game.make_move()
            clear_console()
            winner = self.is_winner()
            if winner:
                print("Player {} wins!!!".format(winner + 1))
                print(self.field_with_ships(0))
                print(self.field_with_ships(1))
                break


if __name__ == '__main__':
    # start the game
    clear_console()
    game = Game()
    game.play()
