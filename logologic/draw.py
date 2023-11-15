from PIL import Image, ImageDraw


class LogoCanvas:
    def __init__(self, size: tuple[int, int] = (500, 500), gridsize: int = 20):
        self.size = size
        self.gridsize = gridsize

        self.image = Image.new('RGBA', size, (255, 255, 255, 255))
        self.image_draw = ImageDraw.Draw(self.image)

        self.draw_grid()

    def draw_grid(self):
        """
        Draws the grid to the canvas
        :return: None
        """
        for column in range(self.gridsize):
            shape = ((0, self.size[1] / self.gridsize * column), (self.size[0], self.size[1] / self.gridsize * column))
            self.image_draw.line(shape, "#BBBBBB")

        for column in range(self.gridsize):
            shape = ((self.size[0] / self.gridsize * column, 0), (self.size[0] / self.gridsize * column, self.size[1]))
            self.image_draw.line(shape, "#BBBBBB")

    def draw_line(self, position_a: tuple[int, int], position_b: tuple[int, int],
                  pensize: int = 1, color: tuple[int, int, int] = (0, 0, 0, 255)):
        """
        Draws a line in the canvas
        :param position_a: tuple[int, int]: First position
        :param position_b: tuple[int, int]: Final position
        :param pensize: int: Width of the line
        :param color: tuple[int, int, int]: Color of the line rgb
        :return: None
        """
        self.image_draw.line((position_a, position_b), width=pensize, fill=color)

    def draw_circle(self, position: tuple[int, int], radius: int,
                    pensize: int = 1, color: tuple[int, int, int] = (0, 0, 0, 255)):
        """
        Draws a circle in the canvas
        :param position: tuple[int, int]: Circle center position
        :param radius: int: Radius of the circle
        :param pensize: int: Width of the line
        :param color: tuple[int, int, int]: Color of the line rgb
        :return: None
        """
        shape = ((position[0] - radius - pensize / 2, position[1] - radius - pensize / 2),
                 (position[0] + radius + pensize / 2, position[1] + radius + pensize / 2))
        self.image_draw.arc(shape, start=0, end=360, width=pensize, fill=color)
