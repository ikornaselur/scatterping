import math
from typing import List

MapType = List[List[int]]


BRAILLE_BASE = 0x2800


class Braille:
    char_map: MapType

    def __init__(self, pixel_map: MapType = None) -> None:
        if pixel_map is None:
            return

        width = math.ceil(len(pixel_map[0]) / 2)
        height = math.ceil(len(pixel_map) / 4)

        self.char_map = [[0 for _ in range(width)] for _ in range(height)]

        for y, row in enumerate(pixel_map):
            for x, pixel in enumerate(row):
                if pixel:

                    char_x = math.floor(x / 2)
                    char_y = math.floor(y / 4)
                    self.char_map[char_y][char_x] |= self._map_pixel(x, y)

    def get_frame(self) -> str:
        return "\n".join(
            "".join(chr(BRAILLE_BASE + c) for c in row) for row in self.char_map
        )

    @staticmethod
    def _map_pixel(x: int, y: int) -> int:
        if y % 4 == 0:
            return 0x8 if x % 2 else 0x1
        if y % 4 == 1:
            return 0x10 if x % 2 else 0x2
        if y % 4 == 2:
            return 0x20 if x % 2 else 0x4
        return 0x80 if x % 2 else 0x40
