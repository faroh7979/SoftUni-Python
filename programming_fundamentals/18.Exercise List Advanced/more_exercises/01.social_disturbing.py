population = input()
wealth = int(input())
population_list = list(map(int, population.split(', ')))
possible_distribution = True
difference = 0

for current_element in range(0, len(population_list)):
    if population_list[current_element] < wealth:
        difference = wealth - population_list[current_element]
        for wealth_element in range(len(population_list) - 1, - 1, - 1):
            rest = population_list[wealth_element] - wealth
            if rest >= difference:
                population_list[current_element] += difference
                population_list[wealth_element] -= difference
                break
            else:
                population_list[current_element] += rest
                population_list[wealth_element] -= rest
                continue
for element in population_list:
    if element < wealth:
        possible_distribution = False
        break
if possible_distribution:
    print(population_list)
else:
    print('No equal distribution possible')
