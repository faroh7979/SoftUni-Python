kind_of_fuel = input()
total_liters_fuel = float(input())

if kind_of_fuel == "Diesel":
    if total_liters_fuel >= 25:
        print(f"You have enough {kind_of_fuel.lower()}.")
    else:
        print(f"Fill your tank with {kind_of_fuel.lower()}!")
elif kind_of_fuel == "Gasoline":
    if total_liters_fuel >= 25:
        print(f"You have enough {kind_of_fuel.lower()}.")
    else:
        print(f"Fill your tank with {kind_of_fuel.lower()}!")
elif kind_of_fuel == "Gas":
    if total_liters_fuel >= 25:
        print(f"You have enough {kind_of_fuel.lower()}.")
    else:
        print(f"Fill your tank with {kind_of_fuel.lower()}!")
else:
    print("Invalid fuel!")
