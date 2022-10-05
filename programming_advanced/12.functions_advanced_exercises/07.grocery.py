def grocery_store(**kwargs):
    product_dict = {}
    for key, value in kwargs.items():
        product_dict[key] = value

    final_dict = dict(sorted(product_dict.items(), key=lambda x: (-(x[1]), -len(x[0]), x[0])))

    final_string = ''
    for key, value in final_dict.items():
        final_string += f'{key}: {value}\n'

    return final_string


print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))

