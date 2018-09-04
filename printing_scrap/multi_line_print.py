import sys
import time


def clear_lines(n_lines):
    default_string = "\033[99m"

    for line in range(n_lines):
        sys.stdout.write("\033[F")  # Move cursor up one line
        sys.stdout.write("\033[K")  # Clear to end of line
    sys.stdout.write(default_string)  # Reset coloring


def character(n_chars):

    red_string = "\033[91m"
    default_string = "\033[99m"

    sys.stdout.write(default_string)
    print("=====")
    sys.stdout.write(red_string)
    print("{}".format(n_chars * ">"))
    sys.stdout.write(default_string)
    print("=====")
    sys.stdout.write(default_string)

    time.sleep(.5)


if __name__ == "__main__":
    for i in range(5):
        character(i)
        clear_lines(3)

    character(i + 1)

