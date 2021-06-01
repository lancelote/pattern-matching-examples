def bar(x):
    match x:
        case ["get", obj] | ["pick", obj] | ["move", obj]:  # <- "all" obj are used
            print(obj)
