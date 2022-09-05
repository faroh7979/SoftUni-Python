def even(length: int):
    if length % 2 == 0:
        return True
    return False


word_list = input().split(" ")
seven_words = [current_word for current_word in word_list if even(len(current_word))]
print("\n".join(seven_words))
