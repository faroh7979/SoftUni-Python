numbers_dictionary = {}

line = input()
while line != "Search":
    number_as_string = line

    # in case of input which it is not an integer
    try:
        number = int(input())
        numbers_dictionary[number_as_string] = number
    except ValueError:
        print("The variable number must be an integer")

    line = input()

line = input()
while line != "Remove":
    searched = line

    # in case of invalid dictionary key
    try:
        print(numbers_dictionary[searched])
    except KeyError:
        print('Number does not exist in dictionary')

    line = input()

line = input()
while line != "End":
    searched = line

    # in case of invalid dictionary key
    try:
        del numbers_dictionary[searched]
    except KeyError:
        print('Number does not exist in dictionary')

    line = input()

print(numbers_dictionary)
