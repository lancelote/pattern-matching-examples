class Foo:
    ...


def foo(param):
    match param:
        case Foo:  # <- should be warning
            ...


if __name__ == "__main__":
    foo(Foo())
