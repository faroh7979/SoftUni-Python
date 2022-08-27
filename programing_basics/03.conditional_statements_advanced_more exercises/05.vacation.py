budget = float(input())
season = input()
location = ""
kind_of_room = ""
price = 0

if budget <= 1000:
    kind_of_room = "Camp"
    if season == "Summer":
        location = "Alaska"
        price = budget * 0.65
    elif season == "Winter":
        location = "Morocco"
        price = budget * 0.45
elif 1000 < budget <= 3000:
    kind_of_room = "Hut"
    if season == "Summer":
        location = "Alaska"
        price = budget * 0.80
    elif season == "Winter":
        location = "Morocco"
        price = budget * 0.60
elif budget > 3000:
    kind_of_room = "Hotel"
    if season == "Summer":
        location = "Alaska"
        price = budget * 0.90
    elif season == "Winter":
        location = "Morocco"
        price = budget * 0.90
print(f"{location} - {kind_of_room} - {price:.2f}")
