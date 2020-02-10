import math
from typing import List

MapType = List[List[int]]


BRAILLE_BASE = 0x2800


class Braille:
    pixel_map: MapType
    char_map: MapType

    def __init__(self, pixel_map: MapType = None) -> None:
        if pixel_map is None:
            return

        width = math.ceil(len(pixel_map[0]) / 2)
        height = math.ceil(len(pixel_map) / 4)

        self.char_map = [[0] * width] * height

        for y, row in enumerate(pixel_map):
            for x, pixel in enumerate(row):
                if pixel:
                    char_x = math.floor(x / 2)
                    char_y = math.floor(y / 4)
                    if x % 2 == 0:
                        if y % 4 == 0:
                            self.char_map[char_y][char_x] |= 0x1
                        elif y % 4 == 1:
                            self.char_map[char_y][char_x] |= 0x2
                        elif y % 4 == 2:
                            self.char_map[char_y][char_x] |= 0x4
                        elif y % 4 == 3:
                            self.char_map[char_y][char_x] |= 0x40
                    else:
                        if y % 4 == 0:
                            self.char_map[char_y][char_x] |= 0x8
                        elif y % 4 == 1:
                            self.char_map[char_y][char_x] |= 0x10
                        elif y % 4 == 2:
                            self.char_map[char_y][char_x] |= 0x20
                        elif y % 4 == 3:
                            self.char_map[char_y][char_x] |= 0x80

    def get_frame(self) -> str:
        return "\n".join(
            "".join(chr(BRAILLE_BASE + c) for c in row) for row in self.char_map
        )
