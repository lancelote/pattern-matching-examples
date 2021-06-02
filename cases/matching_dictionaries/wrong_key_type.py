class Bar:
    ...


def foo(param):
    bar = Bar()

    match param:
        case {bar: "one"}:  # <- syntax error
            print("match")


if __name__ == "__main__":
    foo({2: "one"})
