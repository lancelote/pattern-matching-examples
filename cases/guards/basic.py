def sort(seq):
    match seq:
        case [] | [_]:
            return seq
        case [x, y] if x <= y:
            return seq
        case [x, y]:
            return [y, x]
        case [x, y, z] if x <= y <= z:
            return seq
        case [x, y, z] if x >= y >= z:
            return [z, y, x]
        case [p, *rest]:
            a = sort([x for x in rest if x <= p])
            b = sort([x for x in rest if p < x])
            return a + [p] + b
