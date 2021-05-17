def test(foo):
    match foo:
        case "a" + "b":  # <- should be an error
            pass


if __name__ == '__main__':
    test("ab")
