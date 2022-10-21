def shopping_list(budget: int, **products):
    minimum_budget = 100
    bought_products = 0
    final_print = []

    if minimum_budget > budget:
        return 'You do not have enough budget.'

    for product, values in products.items():
        price, quantity = values
        current_price = float(price) * int(quantity)

        if current_price <= budget:
            budget -= current_price
            bought_products += 1
            final_print.append(f'You bought {product} for {current_price:.2f} leva.\n')

            if bought_products == 5:
                break

    return f'{"".join(final_print)}'


print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))
