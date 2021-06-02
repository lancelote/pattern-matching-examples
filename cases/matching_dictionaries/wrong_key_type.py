class Bar:
    ...


def foo(param):
    bar = Bar()

    match param:
        case {bar: "one"}:  # <- syntax error
            print("match 1")
        case {_: "two"}:  # <- syntax error
            print("match 2")


if __name__ == "__main__":
    foo({2: "one"})
