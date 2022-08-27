first_client_number = int(input())
second_client_number = int(input())
third_client_number = int(input())

if first_client_number >= second_client_number:
    if first_client_number >= third_client_number:
        print(first_client_number)
    else:
        print(third_client_number)
else:
    if second_client_number >= third_client_number:
        print(second_client_number)
    else:
        print(third_client_number)
