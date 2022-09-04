def average(workers: list):
    total = sum(workers)
    count = len(workers)
    average_list = total / count
    return average_list


happiness = list(map(int, input().split(' ')))
improvement_factor = int(input())
improved_happiness = [employer * improvement_factor for employer in happiness]
happy_list = [happy_worker for happy_worker in improved_happiness if happy_worker >= average(improved_happiness)]
if len(improved_happiness) / len(happy_list) <= 2:
    print(f"Score: {len(happy_list)}/{len(improved_happiness)}. Employees are happy!")
else:
    print(f"Score: {len(happy_list)}/{len(improved_happiness)}. Employees are not happy!")
