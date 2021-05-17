def test(foo):
    match foo:
        case [(1, 2 as bar) as bar, (3, 4) as bar] :
            print(bar)


if __name__ == '__main__':
    test([(1, 2), (3, 4)])
