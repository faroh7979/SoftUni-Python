def loading_bar(num: int):
    percentage_count = num // 10
    percentage_string = ''
    comma_count = (100 - num) // 10
    comma_string = ''
    if num != 100:
        return f"{num}% [{percentage_count * '%'}{comma_count * '.'}] \nStill loading..."
    return f"{num}% Complete! \n[{percentage_count * '%'}]"


progress = int(input())
print(loading_bar(progress))
