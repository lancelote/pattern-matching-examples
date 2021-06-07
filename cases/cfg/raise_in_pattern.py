def foo(param):
    match param:
        case 1:
            ...
        case 2:
            raise ValueError

    print(1)  # <- no warning
