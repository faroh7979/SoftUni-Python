total_guests = int(input())

vip_guests = set()
regular_guests = set()

for _ in range(total_guests):
    guest_code = input()

    if guest_code[0].isdigit():
        vip_guests.add(guest_code)

    else:
        regular_guests.add(guest_code)

while True:
    command = input()

    if command == 'END':
        break

    if command[0].isdigit():
        vip_guests.discard(command)

    else:
        regular_guests.discard(command)

total_unattended_guests = len(vip_guests) + len(regular_guests)
print(total_unattended_guests)

if vip_guests:
    print("\n".join(sorted(vip_guests)))
if regular_guests:
    print("\n".join(sorted(regular_guests)))
