def foo():
    match [1, 2, 3]:
        case *first, x:
            print(first, x)


if __name__ == '__main__':
    foo()
