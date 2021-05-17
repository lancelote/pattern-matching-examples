def simplify(expr):
    match expr:
        case ('+', 0, x):
            return x
        case ('+' | '-', x, 0):
            return x
        case ('and', True, x):
            return x
        case ('and', False, x):
            return False
        case ('or', False, x):
            return x
        case ('or', True, x):
            return True
        case ('not', ('not', x)):
            return x
    return expr
