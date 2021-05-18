class C:
    ...


class D(C):
    ...


def test(d):
    match d:
        case C():  # <- this pattern will match
            print("C match")
        case D():
            print("D match")


if __name__ == '__main__':
    test(D())
