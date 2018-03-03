class Ship:

    def __init__(self, bow=(0, 0), horizontal=True, length=1):
        """
        Ship constructor
        :param bow: tuple with coordinates of left upper corner
        :param horizontal: bool value of ship align
        :param length: length of ship
        """
        self.bow = bow
        self.horizontal = horizontal
        self.__length = length
        self.__hit = [False for i in range(length)]

    def shoot_at(self, coords):
        """
        Mark cell with given coordinates as killed
        :param coords: coordinates of the hit
        """
        x, y = coords
        if self.horizontal:
            self.__hit[y - self.bow[1]] = True
        else:
            self.__hit[x - self.bow[0]] = True

    def is_destroyed(self):
        """
        :return: if ship is completely destroyed
        """
        return all(self.__hit)

    def length(self):
        """
        :return: length of the ship
        """
        return self.__length
