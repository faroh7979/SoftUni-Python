kind_of_fuel = input()
fuel_quantity = float(input())
membership = input()

gasoline_liter = 2.22
diesel_liter = 2.33
gas_liter = 0.93

if membership == "Yes":
    gasoline_liter -= 0.18
    diesel_liter -= 0.12
    gas_liter -= 0.08

gasoline_total_price = gasoline_liter * fuel_quantity
diesel_total_price = diesel_liter * fuel_quantity
gas_total_price = gas_liter * fuel_quantity
discount_as_a_total_price = 1

if fuel_quantity > 25:
    discount_as_a_total_price = 0.9
elif fuel_quantity >= 20:
    discount_as_a_total_price = 0.92
else:
    discount_as_a_total_price = 1

gasoline_total_price *= discount_as_a_total_price
diesel_total_price *= discount_as_a_total_price
gas_total_price *= discount_as_a_total_price

if kind_of_fuel == "Gas":
    print(f"{gas_total_price:.2f} lv.")
elif kind_of_fuel == "Gasoline":
    print(f"{gasoline_total_price:.2f} lv.")
elif kind_of_fuel == "Diesel":
    print(f"{diesel_total_price:.2f} lv.")
