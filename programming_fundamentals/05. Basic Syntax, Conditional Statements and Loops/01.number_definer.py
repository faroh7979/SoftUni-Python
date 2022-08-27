client_number = float(input())

if client_number > 0:
    if client_number < 1:
        print('small positive')
    elif client_number > 1000000:
        print('large positive')
    else:
        print('positive')
elif client_number == 0:
    print('zero')
else:
    if client_number > -1:
        print('small negative')
    elif client_number < -1000000:
        print('large negative')
    else:
        print('negative')
