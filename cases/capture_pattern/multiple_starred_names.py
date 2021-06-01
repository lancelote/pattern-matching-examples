match input():
    case ["drop", *bars, *bazs]:
        #         ^^^^^^^^^^^^ SyntaxError: multiple starred names in sequence pattern
        ...
