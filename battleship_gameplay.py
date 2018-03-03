from battleship_player import Player
from battleship_field import Field
import random
import os


def clear_console():
    """
    Clear console in any OS
    """
    os.system('cls' if os.name == 'nt' else 'clear')


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
