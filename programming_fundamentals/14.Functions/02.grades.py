def evaluate(num):
    result = ' '
    if 2 <= num < 3:
        result = None
    elif 3 <= num < 3.50:
        result = "Poor"
    elif 3.50 <= num < 4.50:
        result = "Good"
    elif 4.50 <= num < 5.50:
        result = "Very Good"
    elif 5.50 <= num <= 6.00:
        result = "Excellent"
    return result


score = float(input())
print(evaluate(score))
