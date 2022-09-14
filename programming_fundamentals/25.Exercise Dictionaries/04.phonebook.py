phonebook = {}

while True:
    contact = input()
    if "-" not in contact:
        break
    contact_added = contact.split("-")
    name = contact_added[0]
    phone_number = contact_added[1]
    phonebook[name] = phone_number

for _ in range(int(contact)):
    searched_name = input()
    if searched_name in phonebook:
        print(f"{searched_name} -> {phonebook[searched_name]}")
    else:
        print(f"Contact {searched_name} does not exist.")
