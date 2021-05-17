def test(foo):
    match foo:
        case f"{foo}":  # <- should be an error
            ...
