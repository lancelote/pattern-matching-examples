def test(foo):
    match foo:
        case [x, y, z] if x <= ya <= z:
            #                  ^^ should be an error
            ...
