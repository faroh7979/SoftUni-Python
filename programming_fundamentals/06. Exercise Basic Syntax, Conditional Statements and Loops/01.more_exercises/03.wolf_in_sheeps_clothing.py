queue = input()
length = len(queue)
wolf_position = queue.find('f', 0, 22222222222)
threaten_sheep = (length - wolf_position + 1) // 7

if wolf_position + 1 == length:
    print('Please go away and stop eating my sheep')
else:
    print(f'Oi! Sheep number {threaten_sheep:.0f}! You are about to be eaten by a wolf!')
