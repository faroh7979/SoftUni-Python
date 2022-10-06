def palindrome(word, index):
    reversed_index = (index * - 1) - 1
    if index != len(word) // 2:
        if word[index] != word[reversed_index]:
            return f'{word} is not a palindrome'
        else:
            return palindrome(word, index + 1)
    return f'{word} is a palindrome'


print(palindrome("peter", 0))
