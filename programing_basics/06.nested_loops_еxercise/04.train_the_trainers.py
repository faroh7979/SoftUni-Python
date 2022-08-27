people_in_jury = int(input())
presentation_name = input()
single_total_evaluate = 0
all_total_evaluate = 0
count_evaluate = 0
while presentation_name != 'Finish':
    for evaluate in range(people_in_jury):
        current_evaluation = float(input())
        count_evaluate += 1
        single_total_evaluate += current_evaluation
        all_total_evaluate += current_evaluation
    average_single_evaluation = single_total_evaluate / people_in_jury
    print(f'{presentation_name} - {average_single_evaluation:.2f}.')
    single_total_evaluate = 0
    presentation_name = input()
all_students_average = all_total_evaluate / count_evaluate
print(f"Student's final assessment is {all_students_average:.2f}.")
