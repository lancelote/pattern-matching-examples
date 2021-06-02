class C:
    ...


def foo():
    c = C()
    c.foo = 1
    c.bar = 2

    match 2:
        case c.foo:
            print(f"{c.foo = }")
        case c.bar:
            print(f"{c.bar = }")


if __name__ == '__main__':
    foo()
