def test(foo):
    match foo:
        case 1:
            bar = 2
        case 2:
            baz = 3
    print(bar, baz)
    #     ^^^^^^^^ should be warnings
