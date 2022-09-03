def palindrome(word: str):
    if word == word[::-1]:
        return True
    return False


word_list = input().split(' ')
palindrome_searched = input()
all_palindrome_list = [word for word in word_list if palindrome(word)]
searched_palindrome_count = word_list.count(palindrome_searched)
print(all_palindrome_list)
print(f'Found palindrome {searched_palindrome_count} times')
