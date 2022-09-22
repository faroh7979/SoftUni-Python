parentheses_input = input()
opening_parentheses = '({['
stack_parentheses = []
valid_sequence = True

for symbol in parentheses_input:

    if symbol in opening_parentheses:
        stack_parentheses.append(symbol)

    else:

        if not stack_parentheses:
            valid_sequence = False
            break

        last_opening_parentheses = stack_parentheses.pop()

        if last_opening_parentheses == '(':
            if symbol != ')':
                valid_sequence = False
                break

            elif last_opening_parentheses == '{':
                if symbol != '}':
                    valid_sequence = False
                    break

            elif last_opening_parentheses == '[':
                if symbol != ']':
                    valid_sequence = False
                    break

if valid_sequence:
    print('YES')
else:
    print('NO')
