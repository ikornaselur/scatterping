import shutil

from scatterping.map import get_frame

if __name__ == "__main__":

    def p(x: int) -> None:
        print(f"Width: {x}")
        print(get_frame(terminal_width=x))

    p(10)
    p(20)
    p(30)
    p(40)
    p(50)
    p(60)
    p(70)
    p(80)
    p(90)
    p(100)

    terminal_width = shutil.get_terminal_size().columns
    print(f"Terminal width: {terminal_width}")
    print(get_frame(terminal_width=terminal_width))
