budget = float(input())
season = input()

destination = ""
vacation_type = ""
expense = 0

if budget <= 100:
    if season == "summer":
        destination = "Bulgaria"
        vacation_type = "Camp"
        expense = budget * 0.3
    elif season == "winter":
        destination = "Bulgaria"
        vacation_type = "Hotel"
        expense = budget * 0.7
elif budget <= 1000:
    if season == "summer":
        destination = "Balkans"
        vacation_type = "Camp"
        expense = budget * 0.4
    elif season == "winter":
        destination = "Balkans"
        vacation_type = "Hotel"
        expense = budget * 0.8
elif budget > 1000:
    if season == "summer":
        destination = "Europe"
        vacation_type = "Hotel"
        expense = budget * 0.9
    elif season == "winter":
        destination = "Europe"
        vacation_type = "Hotel"
        expense = budget * 0.9
print(f"Somewhere in {destination}")
print(f"{vacation_type} - {expense:.2f}")
