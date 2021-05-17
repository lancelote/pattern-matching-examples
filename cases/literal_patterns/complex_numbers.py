def test(foo):
    match foo:
        case -3 + 4j as number:  # <- no warning
            print(number)


if __name__ == '__main__':
    test(-3 + 4j)
