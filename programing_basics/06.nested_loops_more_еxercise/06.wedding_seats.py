last_sector = input()
first_sector_total_rows = int(input())
sits_odd_row = int(input())
sits_even_row = sits_odd_row + 2
total_rows = first_sector_total_rows - 1
total_place = 0
for sector in range(65, ord(last_sector) + 1):
    total_rows += 1
    for row in range(1, total_rows + 1):
        if row % 2 == 0:
            for place in range(1, sits_even_row + 1):
                place_letter = place + 96
                print(f'{chr(sector)}{row}{chr(place_letter)}')
                total_place += 1
        else:
            for place in range(1, sits_odd_row + 1):
                place_letter = place + 96
                print(f'{chr(sector)}{row}{chr(place_letter)}')
                total_place += 1
print(total_place)
