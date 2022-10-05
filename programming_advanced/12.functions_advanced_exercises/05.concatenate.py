def concatenate(*args, **kwargs):
    string = ''
    for element in args:
        string += element

    for key, value in kwargs.items():
        if key in string:
            string = string.replace(key, value)

    return string

