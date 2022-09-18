input_phrase = input()
unique_symbols = set()

for symbol in input_phrase:
    unique_symbols.add(symbol)

ordered_list = [new_symbol for new_symbol in sorted(unique_symbols)]

for element in ordered_list:
    matched_times = input_phrase.count(element)
    print(f'{element}: {matched_times} time/s')
