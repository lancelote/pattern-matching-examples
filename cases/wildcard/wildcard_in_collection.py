def foo(param):
    match param:
        case [start, * _, end]:
            print(start, end)


if __name__ == '__main__':
    foo([1, 2, 3, 4, 5])
