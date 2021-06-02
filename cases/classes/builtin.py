def foo(param):
    match param:
        case str():
            print("string")
        case dict() as my_dict:
            print(f"dictionary {my_dict=}")


if __name__ == '__main__':
    foo({1: 2})
