from collections import deque

egg_collection = deque(map(int, input().split(', ')))  # should take the first object
paper_collection = deque(map(int, input().split(', ')))  # should take the last object

box_size = 50
total_filled_boxes = 0

while egg_collection and paper_collection:
    current_egg = egg_collection.popleft()
    current_paper = paper_collection.pop()

    if current_egg == 13:
        paper_collection.appendleft(current_paper)

    elif current_egg <= 0:
        paper_collection.append(current_paper)

    elif current_egg + current_paper <= box_size:
        total_filled_boxes += 1

if total_filled_boxes > 0:
    print(f'Great! You filled {total_filled_boxes} boxes.')
else:
    print("Sorry! You couldn't fill any boxes!")

print(f'Eggs left: {", ".join(map(str, egg_collection))}') if egg_collection else ""
print(f'Pieces of paper left: {", ".join(map(str, paper_collection))}') if paper_collection else ""
