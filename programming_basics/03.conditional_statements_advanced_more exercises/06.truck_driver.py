season = input()
monthly_distance_km = float(input())
salary_km = 0

if monthly_distance_km <= 5000:
    if season == "Spring" or season == "Autumn":
        salary_km = 0.75
    elif season == "Summer":
        salary_km = 0.90
    elif season == "Winter":
        salary_km = 1.05
elif 5000 < monthly_distance_km <= 10000:
    if season == "Spring" or season == "Autumn":
        salary_km = 0.95
    elif season == "Summer":
        salary_km = 1.10
    elif season == "Winter":
        salary_km = 1.25
elif 10000 < monthly_distance_km <= 20000:
    salary_km = 1.45
total_salary = salary_km * monthly_distance_km * 4
net_salary = total_salary * 0.9
print(f"{net_salary:.2f}")
