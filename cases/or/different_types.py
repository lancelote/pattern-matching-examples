def test(foo):
    match foo:
        case 1 | "1" as bar:
            print(bar)
            #     ^^^ should be Union[str, int]
