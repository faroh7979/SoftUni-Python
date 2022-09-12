products = input().split()
bakery_dict = {}
searching_product = input().split()

for element in range(0, len(products), 2):
    bakery_dict[products[element]] = int(products[element + 1])

for searching_element in searching_product:
    if searching_element in bakery_dict:
        value = bakery_dict[searching_element]
        print(f"We have {value} of {searching_element} left")
    else:
        print(f"Sorry, we don't have {searching_element}")
