from scatterping.braille import Braille


def test_braille_dot_1() -> None:
    braille = Braille([[1, 0], [0, 0], [0, 0], [0, 0]])
    assert braille.get_frame() == "⠁"


def test_braille_dot_2() -> None:
    braille = Braille([[0, 0], [1, 0], [0, 0], [0, 0]])
    assert braille.get_frame() == "⠂"


def test_braille_dot_3() -> None:
    braille = Braille([[0, 0], [0, 0], [1, 0], [0, 0]])
    assert braille.get_frame() == "⠄"


def test_braille_dot_4() -> None:
    braille = Braille([[0, 1], [0, 0], [0, 0], [0, 0]])
    assert braille.get_frame() == "⠈"


def test_braille_dot_5() -> None:
    braille = Braille([[0, 0], [0, 1], [0, 0], [0, 0]])
    assert braille.get_frame() == "⠐"


def test_braille_dot_6() -> None:
    braille = Braille([[0, 0], [0, 0], [0, 1], [0, 0]])
    assert braille.get_frame() == "⠠"


def test_braille_dot_7() -> None:
    braille = Braille([[0, 0], [0, 0], [0, 0], [1, 0]])
    assert braille.get_frame() == "⡀"


def test_braille_dot_8() -> None:
    braille = Braille([[0, 0], [0, 0], [0, 0], [0, 1]])
    assert braille.get_frame() == "⢀"


def test_braille_dot_1358() -> None:
    braille = Braille([[1, 0], [0, 1], [1, 0], [0, 1]])
    assert braille.get_frame() == "⢕"


def test_braille_filled() -> None:
    braille = Braille([[1, 1], [1, 1], [1, 1], [1, 1]])
    assert braille.get_frame() == "⣿"


def test_braille_empty() -> None:
    braille = Braille([[0, 0], [0, 0], [0, 0], [0, 0]])
    assert braille.get_frame() == "⠀"


def test_braille_two_columns() -> None:
    braille = Braille([[1, 0, 1, 0], [1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 0, 1]])
    assert braille.get_frame() == "⢣⢕"


def test_braille_two_rows() -> None:
    braille = Braille([[1, 0], [1, 0], [0, 1], [0, 1], [1, 0], [0, 1], [1, 0], [0, 1]])
    assert braille.get_frame() == "⢣\n⢕"


def test_braille_diagonal() -> None:
    braille = Braille(
        [
            [1, 0, 0, 0, 0, 0, 0, 1],
            [0, 1, 0, 0, 0, 0, 1, 0],
            [0, 0, 1, 0, 0, 1, 0, 0],
            [0, 0, 0, 1, 1, 0, 0, 0],
            [0, 0, 0, 1, 1, 0, 0, 0],
            [0, 0, 1, 0, 0, 1, 0, 0],
            [0, 1, 0, 0, 0, 0, 1, 0],
            [1, 0, 0, 0, 0, 0, 0, 1],
        ]
    )
    # fmt: off
    assert braille.get_frame() == "\n".join([
        "⠑⢄⡠⠊",
        "⡠⠊⠑⢄",
    ])
    # fmt: on


def test_braille_globe() -> None:
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
    # fmt: off
    assert braille.get_frame() == "\n".join([
        "⠀⢠⠒⣉⠕⢲⢉⠆",
        "⢀⢗⠉⠀⠀⢀⠇⠀",
        "⠣⠬⠒⠤⠔⠊⠀⠀",
    ])
    # fmt: on
