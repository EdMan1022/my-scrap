import time

from printing_scrap.clear_terminal import clear_term


def frame():
    time.sleep(.5)
    clear_term()


class StickFigure(object):

    def __init__(self):
        self.line_1 = "( )"
        self.line_2 = " | "
        self.line_3_a = "\\|/"
        self.line_3_b = "-|-"
        self.line_4 = " | "
        self.line_5_a = "/ \\"
        self.line_5_b = "||"

        self.state_1 = [self.line_1, self.line_2, self.line_3_a, self.line_4,
                        self.line_5_a]
        self.state_2 = [
            self.line_1,
            self.line_2,
            self.line_3_b,
            self.line_4,
            self.line_5_b
        ]
        self.state_list = [self.state_1, self.state_2]

        self.frame = self.frame_gen()

    def frame_gen(self):
        while True:
            index = 0
            while index < len(self.state_list):
                yield self.state_list[index]
                index += 1

    @property
    def state(self):
        return next(self.frame)

    def render(self):
        return '\n'.join(self.state)


def main():
    clear_term()
    stick_figure = StickFigure()
    for i in range(10):
        print(stick_figure.render())
        frame()
        print(stick_figure.render())
        frame()


if __name__ == "__main__":
    main()
