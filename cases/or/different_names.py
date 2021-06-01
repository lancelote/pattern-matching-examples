def foo(x):
    match x:
        case ["foo", x] | ["bar", y]:  # <- SyntaxError: alternative patterns bind different names
            ...
