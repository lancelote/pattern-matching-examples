class Point:
    ...


def test(foo):
    match foo:
        case Point(0 | 1, 0 | 1):
            print("A corner of the unit square")
