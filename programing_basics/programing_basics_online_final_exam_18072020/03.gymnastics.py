country = input()
discipline = input()
difficulty_evaluation = 0
performance_evaluation = 0

if country == "Russia":
    if discipline == "ribbon":
        difficulty_evaluation = 9.100
        performance_evaluation = 9.400
    elif discipline == "hoop":
        difficulty_evaluation = 9.300
        performance_evaluation = 9.800
    elif discipline == "rope":
        difficulty_evaluation = 9.600
        performance_evaluation = 9.000
elif country == "Bulgaria":
    if discipline == "ribbon":
        difficulty_evaluation = 9.600
        performance_evaluation = 9.400
    elif discipline == "hoop":
        difficulty_evaluation = 9.550
        performance_evaluation = 9.750
    elif discipline == "rope":
        difficulty_evaluation = 9.500
        performance_evaluation = 9.400
elif country == "Italy":
    if discipline == "ribbon":
        difficulty_evaluation = 9.200
        performance_evaluation = 9.500
    elif discipline == "hoop":
        difficulty_evaluation = 9.450
        performance_evaluation = 9.350
    elif discipline == "rope":
        difficulty_evaluation = 9.700
        performance_evaluation = 9.150
sum_evaluation = difficulty_evaluation + performance_evaluation
percentage_to_maximum = 100 - (sum_evaluation / 20 * 100)
print(f"The team of {country} get {sum_evaluation:.3f} on {discipline}.")
print(f"{percentage_to_maximum:.2f}%")
