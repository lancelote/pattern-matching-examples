def foo(param):
    match param:
        case {1: _} as my_dic:
            print(my_dic)
        case {2: _}:
            ...


if __name__ == "__main__":
    foo({1: "one"})
