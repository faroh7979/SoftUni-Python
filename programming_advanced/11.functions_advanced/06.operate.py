def operate(operator, *args):
    def summing():
        return sum(args)

    def subtraction():
        result = args[0]
        for cur_index in range(1, len(args)):
            result -= args[cur_index]

        return result

    def multiply():
        result = 1
        for element in args:
            result *= element

        return result

    def division():
        result = args[0]
        for cur_index in range(1, len(args)):
            result /= args[cur_index]

        return result

    if operator == '+':
        return summing()

    elif operator == '-':
        return subtraction()

    elif operator == '*':
        return multiply()

    elif operator == '/':
        return division()


