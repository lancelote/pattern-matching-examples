def test(foo, bar):
    match foo:
        case 1:
            match bar:
                case 1:
                    ...
                case 2:
                    print(1, 2)
        case 2:
            ...


if __name__ == "__main__":
    test(1, 2)
