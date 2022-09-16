math_expression = input()
parentheses_list = []

for index, symbol in enumerate(math_expression):
    if symbol == '(':
        parentheses_list.append(index)
    elif symbol == ')':
        print(math_expression[parentheses_list.pop():index + 1])
