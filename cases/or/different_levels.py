def simplify(expr):
    match expr:
        case ('/', 0, 0):
            return expr
        case ('*' | '/', 0, _):
            return 0
        case ('+' | '-', x, 0) | ('+', 0, x) | ('*', 1, x) | ('*' | '/', x, 1):
            return x
    return expr
