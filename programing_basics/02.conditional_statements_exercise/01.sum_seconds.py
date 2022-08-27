first_p = int(input())
second_p = int(input())
third_p = int(input())

total_time_second = first_p + second_p + third_p
total_minutes = total_time_second // 60
total_second = total_time_second % 60

if total_second < 10:
    print(f"{total_minutes}:0{total_second}")
else:
    print(f"{total_minutes}:{total_second}")
