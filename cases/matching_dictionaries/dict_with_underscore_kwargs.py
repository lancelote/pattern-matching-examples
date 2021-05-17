def match_dict_with_kwargs(my_dict):
    match my_dict:
        case {"foo": foo, "bar": bar, **_}:
            #                           ^ should be an error
            pass
