def test(foo):
    match foo:
        case 1 or "1":  # <- expected error
            ...
