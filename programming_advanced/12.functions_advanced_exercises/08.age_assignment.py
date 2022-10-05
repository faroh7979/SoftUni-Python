def age_assignment(*args, **kwargs):
    person_dict = {}

    for key, value in kwargs.items():
        for word in args:
            if key == word[0]:
                person_dict[word] = value
                break

    person_dict = dict(sorted(person_dict.items(), key=lambda x: x[0]))

    final_string = ''
    for key, value in person_dict.items():
        final_string += f'{key} is {value} years old.\n'

    return final_string


print(age_assignment("Peter", "George", G=26, P=19))
