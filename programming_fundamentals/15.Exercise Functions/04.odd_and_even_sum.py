def digits_sum(number: int):
    even_sum = 0
    odd_sum = 0
    for current_digit in str(number):
        if int(current_digit) % 2 == 0:
            even_sum += int(current_digit)
        else:
            odd_sum += int(current_digit)
    return f'Odd sum = {odd_sum}, Even sum = {even_sum}'


client_int = int(input())
print(digits_sum(client_int))
