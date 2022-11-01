total_pieces = int(input())
pieces_dictionary = {}

for current_pieces in range(total_pieces):
    command_line = input()
    current_piece, current_composer, current_key = command_line.split('|')
    pieces_dictionary[current_piece] = {'composer': current_composer, 'key': current_key}
while True:
    command_action = input()
    if command_action == 'Stop':
        break
    command_action_split = command_action.split('|')
    command_type = command_action_split[0]
    if command_type == 'Add':
        new_piece_add = command_action_split[1]
        new_composer = command_action_split[2]
        new_key_add = command_action_split[3]
        if new_piece_add in pieces_dictionary:
            print(f"{new_piece_add} is already in the collection!")
        else:
            pieces_dictionary[new_piece_add] = {'composer': new_composer, 'key': new_key_add}
            print(f"{new_piece_add} by {new_composer} in {new_key_add} added to the collection!")
    elif command_type == 'Remove':
        new_piece = command_action_split[1]
        if new_piece in pieces_dictionary:
            pieces_dictionary.pop(new_piece)
            print(f"Successfully removed {new_piece}!")
        else:
            print(f"Invalid operation! {new_piece} does not exist in the collection.")
    elif command_type == 'ChangeKey':
        change_piece = command_action_split[1]
        new_key = command_action_split[2]
        if change_piece in pieces_dictionary:
            pieces_dictionary[change_piece]['key'] = new_key
            print(f"Changed the key of {change_piece} to {new_key}!")
        else:
            print(f"Invalid operation! {change_piece} does not exist in the collection.")
for key in pieces_dictionary:
    print(f"{key} -> Composer: {pieces_dictionary[key]['composer']}, Key: {pieces_dictionary[key]['key']}")
