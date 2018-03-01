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

    def
