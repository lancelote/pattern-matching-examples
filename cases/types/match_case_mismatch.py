def test(foo: int) -> None:
    match foo:
        case "1":  # <= foo is int!
            ...
