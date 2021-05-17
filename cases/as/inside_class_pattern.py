from _ast import BinOp


def test(foo):
    match foo:
        case BinOp("+" | "-" as op):
            print(op)
