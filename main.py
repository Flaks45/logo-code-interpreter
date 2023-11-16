import glob
from PIL import Image

from logologic import Turtle, LogoCanvas, \
    logo_fd, logo_bk, logo_rt, logo_lt, logo_color, logo_setpensize, logo_circle, logo_setxy
from code_exctractor import get_logo_tokens_from_file


def make_gif(frame_folder):
    frames = [Image.open(image).convert('RGB') for image in glob.glob(f"{frame_folder}/*.PNG")]
    frame_one = frames[0]
    frame_one.save("./assets/output.gif", format="GIF", append_images=frames, save_all=True, duration=100)


if __name__ == "__main__":
    canvas = LogoCanvas()
    turtle = Turtle(250, 250, 270)

    functions = {
        "fd": lambda: logo_fd(canvas, turtle, value),
        "bk": lambda: logo_bk(canvas, turtle, value),
        "rt": lambda: logo_rt(canvas, turtle, value),
        "lt": lambda: logo_lt(canvas, turtle, value),
        "color": lambda: logo_color(canvas, turtle, value),
        "setpensize": lambda: logo_setpensize(canvas, turtle, value),
        "circle": lambda: logo_circle(canvas, turtle, value),
        "setxy": lambda: logo_setxy(canvas, turtle, value)
    }

    instructions = get_logo_tokens_from_file("./logo_code_example.txt", tuple(functions.keys()))

    for index, instruction in enumerate(instructions):
        value = instruction[1]
        functions[instruction[0]]()

        canvas.image.save(f"./assets/frames/frame{index:05}.PNG")

    make_gif("./assets/frames/")
