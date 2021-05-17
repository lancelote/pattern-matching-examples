def test(my_dict):
    match my_dict:
        case {"foo": foo, "bar": bar}:
            print(foo, bar)


test({"foo": "foo_value", "bar": "bar_value", "baz": "baz_value"})
