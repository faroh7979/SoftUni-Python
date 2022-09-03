line = input()
vowels = ['a', 'o', 'u', 'e', 'i']
no_vowels = [char for char in line if char.lower() not in vowels]
print(* no_vowels, sep='')
