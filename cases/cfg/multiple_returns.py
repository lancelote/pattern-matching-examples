def foo(param):
    match param:
        case 1:
            return 1
        case 2:
            return 2
        case 3:
            return 3
        case _:
            return 4

    print("hello")  # <- Code is unreachable
