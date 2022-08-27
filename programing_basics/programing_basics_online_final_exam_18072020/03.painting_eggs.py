egg_size = input()
colour_of_painting = input()
total_sets = int(input())
set_single_price = 0

if egg_size == "Large":
    if colour_of_painting == "Red":
        set_single_price = 16
    elif colour_of_painting == "Green":
        set_single_price = 12
    elif colour_of_painting == "Yellow":
        set_single_price = 9
elif egg_size == "Medium":
    if colour_of_painting == "Red":
        set_single_price = 13
    elif colour_of_painting == "Green":
        set_single_price = 9
    elif colour_of_painting == "Yellow":
        set_single_price = 7
elif egg_size == "Small":
    if colour_of_painting == "Red":
        set_single_price = 9
    elif colour_of_painting == "Green":
        set_single_price = 8
    elif colour_of_painting == "Yellow":
        set_single_price = 5
total_price = total_sets * set_single_price
incomes = total_price * 0.65
print(f"{incomes:.2f} leva.")
