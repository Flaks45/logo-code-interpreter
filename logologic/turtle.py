import math


class Turtle:
    """
    Turtle is an imaginary position with values that represents the drawing pointer.
    This class DOES NOT DRAW, it just gives the coordinates and other values
    """
    def __init__(self, xposition: int = 250, yposition: int = 250, rotation: int = 270,
                 color: tuple[int, int, int] = (0, 0, 0), pensize: int = 1):
        self.x = xposition
        self.y = yposition
        self.rotation = rotation
        self.color = color
        self.pensize = pensize

    def get_values(self):
        """
        Gets the values from turtle as dict kwargs
        :return: dictionary: {"x": int, "y": int, "rotation": int, "color": tuple[int, int, int], "pensize": int}
        """
        return {"x": self.x, "y": self.y, "rotation": self.rotation, "color": self.color, "pensize": self.pensize}

    def get_xy(self):
        """
        Gets the values of xy in a manageable format
        :return: tuple[int, int]: Position of the turtle
        """
        return self.x, self.y

    def set_xy(self, position: tuple[int, int]):
        """
        Sets x and y position for the turtle
        :param position: tuple[int, int]: For x and y positions
        :return: tuple[int, int]: New position of turtle
        """
        self.x = position[0]
        self.y = position[1]
        return self.x, self.y

    def set_color(self, rgb_values: tuple[int, int, int]):
        """
        Sets the color for the turtle
        :param rgb_values: tuple[int, int, int]: Red green and blue values (0-255)
        :return: tuple[int, int, int]: New color of turtle
        """
        self.color = rgb_values
        return self.color

    def set_pensize(self, pensize: int):
        """
        Sets the pensize for the turtle
        :param pensize: int: Width of the pensize
        :return: New pensize of turtle
        """
        self.pensize = pensize
        return self.pensize

    def forward(self, distance: int):
        """
        Moves turtle forwards or backwards
        :param distance: int: Distance that the turtle moves
        :return: tuple[int, int]: New position of turtle
        """
        self.x += int(math.cos(math.radians(self.rotation)) * distance)
        self.y += int(math.sin(math.radians(self.rotation)) * distance)
        return self.x, self.y

    def rotate(self, angle: int):
        """
        Rotates turtle (+) clockwise or (-) counterclockwise
        :param angle: int: For rotation addition
        :return: int: New rotation of turtle
        """
        self.rotation += int(angle)
        return self.rotation
