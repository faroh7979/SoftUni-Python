def ticket_status(ticket: str):
    wining_symbols = ['@', '#', '$', '^']
    # copy_wining_symbols = wining_symbols.copy()
    wining_combos = []
    current_winning_symbol = ''
    obtain_winning_symbol = False
    if len(ticket) != 20:
        return "invalid ticket"
    else:
        left_side = ticket[:10]
        right_side = ticket[10:]
        for list_element in wining_symbols:
            if obtain_winning_symbol:
                break
            if list_element in ticket:
                if left_side.count(list_element) > 5 and right_side.count(list_element) > 5:
                    current_winning_symbol = list_element
                    obtain_winning_symbol = True
                    # copy_wining_symbols.remove(current_winning_symbol)
                    # for list_element_new in copy_wining_symbols:
                    #     if list_element_new in ticket:
                    #         return f'ticket "{ticket}" - no match'
                else:
                    continue
                for wining_combo in range(10, 5, -1):
                    wining_combos.append(current_winning_symbol * wining_combo)
        if not obtain_winning_symbol:
            return f'ticket "{ticket}" - no match'
        if wining_combos[0] in left_side and wining_combos[0] in right_side:
            return f'ticket "{ticket}" - 10{current_winning_symbol} Jackpot!'
        else:
            for matching in range(1, 5):
                if wining_combos[matching] in left_side and wining_combos[matching] in right_side:
                    return f'ticket "{ticket}" - {10 - matching}{current_winning_symbol}'
        return f'ticket "{ticket}" - no match'


tickets = input()
tickets_list = [ticket_comprehension.strip() for ticket_comprehension in tickets.split(', ')]

for ticket_last in tickets_list:
    print(ticket_status(ticket_last))
