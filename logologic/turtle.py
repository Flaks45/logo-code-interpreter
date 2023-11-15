import math


class Turtle:
    def __init__(self, xposition: int = 0, yposition: int = 0, rotation: int = 90,
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

    def forward(self, distance: int):
        """
        Moves turtle forwards or backwards
        :return: tuple[int, int]: New position of turtle
        """
        self.x += int(math.cos(math.radians(self.rotation)) * distance)
        self.y += int(math.sin(math.radians(self.rotation)) * distance)
        return (self.x, self.y)

    def rotate(self, angle: int):
        """
        Rotates turtle (-) clockwise or (+) counterclockwise
        :return: int: New rotation of turtle
        """
        self.rotation += int(angle)
        return self.rotation
