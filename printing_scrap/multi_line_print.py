import sys
import time


def clear_lines(n_lines):
    default_string = "\033[99m"

    print(chr(27) + "[2J")

    # for line in range(n_lines):
    #     sys.stdout.write("\033[F")  # Move cursor up one line
    #     sys.stdout.write("\033[K")  # Clear to end of line


def character(n_chars):

    red_string = "\033[91m"
    default_string = "\033[99m"
    black_string = "\033[90m"
    white_string = "\033[97m"

    print("{}=====".format(default_string))
    # sys.stdout.write(red_string)
    print("{}{}".format(red_string, n_chars * ">"))
    # sys.stdout.write(default_string)
    print("{}=====".format(default_string))
    # sys.stdout.write(default_string)

    time.sleep(.5)


if __name__ == "__main__":
    for i in range(5):
        character(i)
        # clear_lines(3)

    character(i + 1)

