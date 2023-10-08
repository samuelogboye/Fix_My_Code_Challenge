#!/usr/bin/python3
"""
A  module that defines a square
"""


class Square():
    """ A class that defines a square
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a new instance of the class with the
        specified width and height.

        Parameters:
            width (int): The width of the object.
                Defaults to 0 if not provided.
            height (int): The height of the object.
                Defaults to 0 if not provided.
        """
        self.width = width
        self.height = height

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def perimiter_of_my_square(self):
        """
        Calculate the perimeter of a square.

        Returns:
            The perimeter of the square.

        Parameters:
            self (Square): An instance of the Square class.

        """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """
        Returns a string representation of the object.
        """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.perimiter_of_my_square())
