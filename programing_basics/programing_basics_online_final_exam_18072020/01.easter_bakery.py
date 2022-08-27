price_flour_kg = float(input())
needed_floar_kg = float(input())
needed_sugar_kg = float(input())
count_core_eggs = int(input())
packages_yeast = int(input())

price_sugar_kg = price_flour_kg * 0.75
price_core_eggs = price_flour_kg * 1.1
price_packages_yeast = price_sugar_kg * 0.2

total_expense = price_packages_yeast * packages_yeast +\
                price_core_eggs * count_core_eggs +\
                price_sugar_kg * needed_sugar_kg +\
                price_flour_kg * needed_floar_kg

print(f"{total_expense:.2f}")
