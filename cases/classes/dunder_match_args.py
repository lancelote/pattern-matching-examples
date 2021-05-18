class Click:
    __match_args__ = ("position", "button")

    def __init__(self, position, button):
        self.position = position
        self.button = button


def main():
    match Click(1, 2):
        case Click(a, b):
            print(a, b)


if __name__ == '__main__':
    main()
