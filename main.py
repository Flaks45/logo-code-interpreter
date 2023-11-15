from logologic import Turtle, LogoCanvas, logo_fd, logo_bk, logo_rt, logo_lt, logo_color, logo_setpensize, logo_circle

if __name__ == "__main__":
    canvas = LogoCanvas()
    turtle = Turtle(250, 250, 270)

    logo_setpensize(canvas, turtle, 5)
    logo_fd(canvas, turtle, 50)
    logo_rt(canvas, turtle, 90)
    logo_fd(canvas, turtle, 50)
    logo_color(canvas, turtle, (255, 0, 0))
    logo_lt(canvas, turtle, 90)
    logo_bk(canvas, turtle, 100)
    logo_circle(canvas, turtle, 50)

    canvas.image.show()
