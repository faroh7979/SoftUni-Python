junior_cyclists = int(input())
senior_cyclists = int(input())
trace_type = input()
total_cyclists = junior_cyclists + senior_cyclists

junior_entry = 0
senior_entry = 0

if trace_type == "trail":
    junior_entry = 5.50
    senior_entry = 7
elif trace_type == "cross-country":
    junior_entry = 8
    senior_entry = 9.50
    if total_cyclists >= 50:
        junior_entry *= 0.75
        senior_entry *= 0.75
elif trace_type == "downhill":
    junior_entry = 12.25
    senior_entry = 13.75
elif trace_type == "road":
    junior_entry = 20
    senior_entry = 21.50
total_incomes = junior_cyclists * junior_entry + senior_cyclists * senior_entry
net_incomes = total_incomes * 0.95
print(f"{net_incomes:.2f}")
