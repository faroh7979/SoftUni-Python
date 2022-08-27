num_1 = int(input())
num_2 = int(input())
user_operator = input()

result = 0
kind_num = ""

if user_operator == "+":
    result = num_1 + num_2
    if result % 2 == 0:
       kind_num = "even"
    else:
        kind_num = "odd"
    print(f"{num_1} + {num_2} = {result} - {kind_num}")
elif user_operator == "-":
    result = num_1 - num_2
    if result % 2 == 0:
       kind_num = "even"
    else:
        kind_num = "odd"
    print(f"{num_1} - {num_2} = {result} - {kind_num}")
elif user_operator == "*":
    result = num_1 * num_2
    if result % 2 == 0:
       kind_num = "even"
    else:
        kind_num = "odd"
    print(f"{num_1} * {num_2} = {result} - {kind_num}")
elif user_operator == "/":
    if num_2 == 0:
        print(f"Cannot divide {num_1} by zero")
    else:
        result = num_1 / num_2
        print(f"{num_1} / {num_2} = {result:.2f}")
elif user_operator == "%":
    if num_2 == 0:
        print(f"Cannot divide {num_1} by zero")
    else:
        result = num_1 % num_2
        print(f"{num_1} % {num_2} = {result}")
