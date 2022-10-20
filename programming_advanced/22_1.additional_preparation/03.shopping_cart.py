def shopping_cart(*product_args):

    limitation_dict = {
        'Soup': 3,
        'Pizza': 4,
        'Dessert': 2
    }

    meal_dict = {}
    final_string = ''

    for element in product_args:

        if element == 'Stop':
            break

        meal, product = element

        if meal not in meal_dict:
            meal_dict[meal] = []

        if product not in meal_dict[meal] and len(meal_dict[meal]) < limitation_dict[meal]:
            meal_dict[meal].append(product)

    if not meal_dict:
        return 'No products in the cart!'

    for key in limitation_dict:
        if key not in meal_dict:
            meal_dict[key] = ''

    meal_dict = dict(sorted(meal_dict.items(), key=lambda x: (-len(x[1]), x[0])))

    for key in meal_dict:
        final_string += f'{key}:\n'
        for value in sorted(meal_dict[key]):
            final_string += f' - {value}\n'

    return final_string


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))
