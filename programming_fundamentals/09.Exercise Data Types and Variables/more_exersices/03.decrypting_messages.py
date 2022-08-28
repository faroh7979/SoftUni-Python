key = int(input())
total_letters = int(input())
decrypted_string = ''

for _ in range(total_letters):
    current_letter = input()
    decrypted_string += chr((ord(current_letter) + key))
print(decrypted_string)
