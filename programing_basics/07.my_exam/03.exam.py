from math import floor
type_of_cat = input()
valid_cat = False
if type_of_cat == "British Shorthair" or type_of_cat == "Siamese" or type_of_cat == "Persian" or type_of_cat == "Ragdoll" or type_of_cat == "American Shorthair" or type_of_cat == "Siberian":
    valid_cat = True
else:
    print(f'{type_of_cat} is invalid cat!')
gender_of_cat = input()
cat_years = 0

if gender_of_cat == 'm':
    if type_of_cat == "British Shorthair":
        cat_years = 13
    elif type_of_cat == "Siamese":
        cat_years = 15
    elif type_of_cat == "Persian":
        cat_years = 14
    elif type_of_cat == "Ragdoll":
        cat_years = 16
    elif type_of_cat == "American Shorthair":
        cat_years = 12
    elif type_of_cat == "Siberian":
        cat_years = 11
else:
    if type_of_cat == "British Shorthair":
        cat_years = 14
    elif type_of_cat == "Siamese":
        cat_years = 16
    elif type_of_cat == "Persian":
        cat_years = 15
    elif type_of_cat == "Ragdoll":
        cat_years = 17
    elif type_of_cat == "American Shorthair":
        cat_years = 13
    elif type_of_cat == "Siberian":
        cat_years = 12
total_month = cat_years * 12
cat_total_month = floor(total_month / 6)
if valid_cat:
    print(f'{cat_total_month} cat months')
