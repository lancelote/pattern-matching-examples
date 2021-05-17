def is_closed(sequence):
    match sequence:
        case [_]:  # any sequence with a single element
            return True
        case [start, * _, end]:  # a sequence with at least two elements
            return start == end
        case _:  # anything
            return False
