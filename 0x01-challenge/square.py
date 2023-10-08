#!/usr/bin/python3

class Square:
    """A class that defines a square"""

    def __init__(self, side_length=0):
        """
        Initializes a new instance of the class with the
        specified side length.

        Parameters:
            side_length (int): The side length of the square.
                Defaults to 0 if not provided.
        """
        self.side_length = side_length

    def area_of_my_square(self):
        """
        Calculates the area of a square.

        Returns:
            int: The area of the square.
        """
        return self.side_length * self.side_length

    def perimeter_of_my_square(self):
        """
        Calculate the perimeter of a square.

        Returns:
            The perimeter of the square.
        """
        return 4 * self.side_length

    def __str__(self):
        """
        Returns a string representation of the object.
        """
        return "{}".format(self.side_length)


if __name__ == "__main__":
    s = Square(side_length=12)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
