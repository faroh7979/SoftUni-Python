client_deck = input().split()
total_faro_shuffling = int(input())
middle_of_the_deck = len(client_deck) // 2
for shuffle in range(total_faro_shuffling):
    shuffled_deck = []
    left_deck_part = client_deck[0:middle_of_the_deck:1]
    right_deck_part = client_deck[middle_of_the_deck:len(client_deck):1]
    for index_card in range(len(left_deck_part)):
        shuffled_deck.append(left_deck_part[index_card])
        shuffled_deck.append(right_deck_part[index_card])
    client_deck = shuffled_deck
print(client_deck)
