def average(*args):
    match args:
        case [x, y]:  # captures the two elements of a sequence
            return (x + y) / 2
        case [x]:  # captures the only element of a sequence
            return x
        case []:
            return 0
        case a:  # captures the entire sequence
            return sum(a) / len(a)
