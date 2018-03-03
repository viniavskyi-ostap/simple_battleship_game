import re


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
            if re.match(r'^([A-J]([1-9]|10))$', move):
                return int(move[1:]) - 1, ord(move[0]) - 65
            else:
                print('Wrong format!!! Try again!')
