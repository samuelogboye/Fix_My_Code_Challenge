#!/usr/bin/python3

class Square():
    """
    A class representing a square shape.

    Attributes:
    - width: The width of the square.
    - height: The height of the square.
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
        """
        Calculates the area of a square.

        Returns:
            int: The area of the square.
        """
        return self.width * self.width

    def perimeter_of_my_square(self):
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
    print(s.perimeter_of_my_square())
