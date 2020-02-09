from os import path

from drawille import Canvas
from reportlab.graphics import renderPM
from svglib.svglib import svg2rlg


def get_cutoff(width: int) -> int:
    if width <= 100:
        return 250
    if width <= 180:
        return 240
    return 230


def get_frame(terminal_width: int = 80) -> str:
    pixel_width = terminal_width * 2
    cutoff = get_cutoff(pixel_width)

    base_path = path.dirname(__file__)
    world_path = path.abspath(path.join(base_path, "world.svg"))

    drawing = svg2rlg(world_path)
    image = renderPM.drawToPIL(drawing)
    height, width = image.size
    image = image.resize((pixel_width, int(width / height * pixel_width)))
    height, width = image.size

    canvas = Canvas()

    for x in range(0, height):
        for y in range(0, width):
            pixel = image.getpixel((x, y))
            if pixel[0] < cutoff and pixel[1] < cutoff and pixel[2] < cutoff:
                canvas.set(x, y)

    return canvas.frame()
