def test(foo):
    match foo:
        case (x, x):
            print(x)
        case (_, _):
            print(_)  # <- should be undefined


if __name__ == '__main__':
    test((1, 1))
