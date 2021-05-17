def test(foo):
    match foo:
        case [(1, 2 as baz) as bar, (3, 4) as egg] if bar and egg:
            print(bar, egg)
        case [int() as first, int() as second]:
            ...


if __name__ == '__main__':
    test([(1, 2), (3, 4)])
