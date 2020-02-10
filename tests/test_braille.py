from scatterping.braille import Braille


def test_braille_first_row_left() -> None:
    braille = Braille([[1, 0], [0, 0], [0, 0], [0, 0]])
    assert braille.get_frame() == "⠁"


def test_braille_second_row_left() -> None:
    braille = Braille([[0, 0], [1, 0], [0, 0], [0, 0]])
    assert braille.get_frame() == "⠂"


def test_braille_third_row_left() -> None:
    braille = Braille([[0, 0], [0, 0], [1, 0], [0, 0]])
    assert braille.get_frame() == "⠄"


def test_braille_fourth_row_left() -> None:
    braille = Braille([[0, 0], [0, 0], [0, 0], [1, 0]])
    assert braille.get_frame() == "⡀"


def test_braille_first_row_right() -> None:
    braille = Braille([[0, 1], [0, 0], [0, 0], [0, 0]])
    assert braille.get_frame() == "⠈"


def test_braille_second_row_right() -> None:
    braille = Braille([[0, 0], [0, 1], [0, 0], [0, 0]])
    assert braille.get_frame() == "⠐"


def test_braille_third_row_right() -> None:
    braille = Braille([[0, 0], [0, 0], [0, 1], [0, 0]])
    assert braille.get_frame() == "⠠"


def test_braille_fourth_row_right() -> None:
    braille = Braille([[0, 0], [0, 0], [0, 0], [0, 1]])
    assert braille.get_frame() == "⢀"


def test_braille_mixed() -> None:
    braille = Braille([[1, 0], [0, 1], [1, 0], [0, 1]])
    assert braille.get_frame() == "⢕"


def test_braille_filled() -> None:
    braille = Braille([[1, 1], [1, 1], [1, 1], [1, 1]])
    assert braille.get_frame() == "⣿"


def test_braille_empty() -> None:
    braille = Braille([[0, 0], [0, 0], [0, 0], [0, 0]])
    assert braille.get_frame() == "⠀"


def test_braille_two_columns() -> None:
    braille = Braille([[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]])
    assert braille.get_frame() == "⣿⣿"


def test_braille_two_rows() -> None:
    braille = Braille([[1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]])
    assert braille.get_frame() == "⣿\n⣿"


def test_braille_diagonal() -> None:
    braille = Braille(
        [
            [1, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 1],
        ]
    )
    assert braille.get_frame() == "⠑⢄  \n  ⠑⢄"


"""
def test_braille_globe_art() -> None:
    pixel_map = [
        [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0],
        [0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0],
        [0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0],
        [0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        [1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    braille = Braille(pixel_map)
    assert braille.get_frame() == ""
"""
