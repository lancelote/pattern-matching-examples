def fib(arg):
    match arg:
        case 0:
            return 1
        case 1:
            return 1
        case n:
            return fib(n - 1) + fib(n - 2)
