command = input()
total_coffee_cups = 0
too_much_events = False

while command != 'END':
    if command.lower() == 'coding' or command.lower() == 'dog' or command.lower() == 'cat' or command.lower() == 'movie':
        if command.isupper():
            total_coffee_cups += 2
        else:
            total_coffee_cups += 1
    command = input()
if total_coffee_cups > 5:
    too_much_events = True
if too_much_events:
    print('You need extra sleep')
else:
    print(total_coffee_cups)
