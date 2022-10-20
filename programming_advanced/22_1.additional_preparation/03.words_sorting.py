def words_sorting(*args):
    word_dict = {}
    final_string = ''

    total_score = 0
    for word in args:
        current_score = 0

        for letter in word:
            current_score += ord(letter)

        word_dict[word] = current_score
        total_score += current_score

    if total_score % 2 != 0:
        word_dict = dict(sorted(word_dict.items(), key=lambda x: -x[1]))

    else:
        word_dict = dict(sorted(word_dict.items(), key=lambda x: x[0]))

    for key, value in word_dict.items():
        final_string += f'{key} - {value}\n'

    return final_string

