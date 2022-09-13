contest_dict = {}
students_score = {}


def password_validation(func_course, func_password, def_dict):
    if def_dict[func_course] == func_password:
        return True
    return False


def valid_contest(func_contest, def_dict_f):
    if func_contest in def_dict_f:
        return True
    return False


while True:
    command = input()
    if command == 'end of contests':
        break
    command_line_split = command.split(':')
    current_course = command_line_split[0]
    current_password = command_line_split[1]
    contest_dict[current_course] = current_password

while True:
    command_line = input()
    if command_line == 'end of submissions':
        break
    command_line_split_split = command_line.split('=>')
    contest = command_line_split_split[0]
    password = command_line_split_split[1]
    username = command_line_split_split[2]
    points = command_line_split_split[3]
    if password_validation(contest, password, contest_dict) and valid_contest(contest, contest_dict):
        temporary_dict = {username: int(points)}
        if contest not in students_score:
            students_score[contest] = temporary_dict
        else:
            if username not in students_score[contest]:
                students_score[contest] = temporary_dict
            else:
                if students_score[contest][username] < int(points):
                    students_score[contest][username] = int(points)

print(contest_dict)
print(students_score)

