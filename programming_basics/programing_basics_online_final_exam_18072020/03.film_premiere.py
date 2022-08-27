movie_name = input()
snack_menu = input()
total_tickets = int(input())
single_ticket = 0

if movie_name == "John Wick":
    if snack_menu == "Drink":
        single_ticket = 12
    elif snack_menu == "Popcorn":
        single_ticket = 15
    elif snack_menu == "Menu":
        single_ticket = 19
elif movie_name == "Star Wars":
    if snack_menu == "Drink":
        single_ticket = 18
    elif snack_menu == "Popcorn":
        single_ticket = 25
    elif snack_menu == "Menu":
        single_ticket = 30
elif movie_name == "Jumanji":
    if snack_menu == "Drink":
        single_ticket = 9
    elif snack_menu == "Popcorn":
        single_ticket = 11
    elif snack_menu == "Menu":
        single_ticket = 14
if movie_name == "Star Wars" and total_tickets >= 4:
    single_ticket *= 0.7
elif movie_name == "Jumanji" and total_tickets == 2:
    single_ticket *= 0.85
total_price = single_ticket * total_tickets
print(f"Your bill is {total_price:.2f} leva.")
