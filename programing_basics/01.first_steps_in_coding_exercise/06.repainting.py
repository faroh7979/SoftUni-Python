needed_nailon_kv_metri = int(input())
needed_paint_liters = int(input())
razreditel_liters = int(input())
need_hours_todo_the_job = int(input())

nailon_price_kv_meter = 1.50
paint_a_liter = 14.50
razreditel_a_liter = 5.00

extra_paint = needed_paint_liters * 10/100
total_paint = needed_paint_liters + extra_paint

extra_nailon_kv_meters = 2
total_nailon = needed_nailon_kv_metri + extra_nailon_kv_meters
bags = 0.40

sum_nailon = total_nailon * nailon_price_kv_meter
sum_paint = total_paint * paint_a_liter
sum_razreditel = razreditel_liters * razreditel_a_liter

consumative_expense = sum_razreditel + sum_paint + sum_nailon +bags
expence_for_workhour = consumative_expense * 30/100
work_expence = expence_for_workhour * need_hours_todo_the_job

total_expence = consumative_expense + work_expence

print(total_expence)
