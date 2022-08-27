count_sweet_bread = int(input())
count_egg_portion = int(input())
mini_sweets_kilograms = int(input())

sweet_bread_lv = 3.20
eggs_per_12_lv = 4.35
mini_sweets_lv_kilogram = 5.40
egg_paint_lv = 0.15

total_egg_expense = count_egg_portion * eggs_per_12_lv + count_egg_portion * 12 * egg_paint_lv
total_sweet_bread_expense = count_sweet_bread * sweet_bread_lv
total_mini_sweets_expense = mini_sweets_kilograms * mini_sweets_lv_kilogram

total_expense = total_egg_expense + total_mini_sweets_expense + total_sweet_bread_expense

print(f"{total_expense:.2f}")
