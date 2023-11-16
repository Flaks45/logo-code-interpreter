from logologic import Turtle, LogoCanvas


def logo_fd(canvas: LogoCanvas, turtle: Turtle, distance: int):
    old_pos = turtle.get_xy()
    new_pos = turtle.forward(distance)
    canvas.draw_line(old_pos, new_pos, turtle.pensize, turtle.color)


def logo_bk(canvas: LogoCanvas, turtle: Turtle, distance: int):
    old_pos = turtle.get_xy()
    new_pos = turtle.forward(-distance)
    canvas.draw_line(old_pos, new_pos, turtle.pensize, turtle.color)


def logo_rt(canvas: LogoCanvas, turtle: Turtle, angle: int):
    turtle.rotate(angle)


def logo_lt(canvas: LogoCanvas, turtle: Turtle, angle: int):
    turtle.rotate(-angle)


def logo_color(canvas: LogoCanvas, turtle: Turtle, color: tuple[int, int, int]):
    turtle.set_color(color)


def logo_setpensize(canvas: LogoCanvas, turtle: Turtle, pensize: int):
    turtle.set_pensize(pensize)


def logo_circle(canvas: LogoCanvas, turtle: Turtle, radius: int):
    canvas.draw_circle(turtle.get_xy(), radius, turtle.pensize, turtle.color)


def logo_setxy(canvas: LogoCanvas, turtle: Turtle, position: tuple[int, int]):
    turtle.set_xy(position)
