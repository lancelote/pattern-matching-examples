def simplify_expr(tokens):
    match tokens:
        case [('(' | '[') as l, * expr, (')' | ']') as r] if (l + r) in ('()', '[]'):
            return simplify_expr(expr)
        case [0, ('+' | '-') as op, right]:
            return UnaryOp(op, right)
        case [(int() | float() as left) | Num(left), '+', (int() | float() as right) | Num(right)]:
            return Num(left + right)
        case [(int() | float()) as value]:
            return Num(value)
