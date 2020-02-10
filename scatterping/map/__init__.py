from dataclasses import dataclass
from os import path
from typing import List

from drawille import Canvas, get_pos
from reportlab.graphics import renderPM
from svglib.svglib import svg2rlg


@dataclass
class Overlay:
    """ A text overlay for the map

    The x,y coordinate is based 0-100% of width,height
    """

    x: int
    y: int
    text: str


def get_cutoff(width: int) -> int:
    if width <= 100:
        return 250
    if width <= 180:
        return 240
    return 230


def set_overlay(canvas: Canvas, height: int, width: int, overlay: Overlay) -> None:
    col, row = get_pos(height * overlay.x / 100, width * overlay.y / 100)

    for i, c in enumerate(overlay.text):
        canvas.chars[row][col + i] = c

    breakpoint()  # noqa: E702 XXX BREAKPOINT!!
    canvas.chars[row].insert(col, "X")


RED = "\u001b[31m"
CLEAR = "\u001b[0m"

EXAMPLE_OVERLAYS = [
    Overlay(x=19, y=33, text="251"),  # Northern Virginia
    Overlay(x=18, y=30, text="251"),  # Ohio
    Overlay(x=6, y=30, text="251"),  # Oregon
    Overlay(x=7, y=33, text="251"),  # Northern California
    Overlay(x=22, y=24, text="251"),  # Montreal
    Overlay(x=29, y=75, text="251"),  # Sao Paulo
    # Europe/Middle East
    Overlay(x=42, y=18, text="251"),  # Ireland
    Overlay(x=44, y=20, text="211"),  # London
    Overlay(x=46, y=23, text="141"),  # Frankfurt
    Overlay(x=45, y=24, text="211"),  # Paris
    Overlay(x=49, y=15, text="312"),  # Stockholm
    Overlay(x=60, y=40, text="384"),  # Bahrain
    # Asia
    Overlay(x=78, y=57, text="666"),  # Singapore
    Overlay(x=88, y=33, text="666"),  # Tokyo
    Overlay(x=92, y=84, text="666"),  # Sydney
    Overlay(x=84, y=32, text="666"),  # Seoul
    Overlay(x=68, y=45, text="666"),  # Mumbai
    Overlay(x=81, y=42, text="666"),  # Hong Kong
]


def get_frame(terminal_width: int = 80, overlays: List[Overlay] = None) -> str:
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

    if overlays is None:
        overlays = EXAMPLE_OVERLAYS

    if overlays:
        for overlay in overlays:
            set_overlay(canvas, height, width, overlay)
            """
            canvas.set_text(
                height * overlay.x / 100,
                width * overlay.y / 100,
                f"{RED}{overlay.text}{CLEAR}",
            )
            """

    return canvas.frame()
