total_pens = int(input())
total_marks = int(input())
quantity_cleaner = int(input())
percentage_discount = int(input())

pens_amount = 5.80
marks_amount = 7.20
cleaner_amount = 1.20

price_pens_discount = (total_pens * pens_amount) - (total_pens * pens_amount * (percentage_discount / 100))
price_marks_discount = (total_marks * marks_amount) - (total_marks * marks_amount * (percentage_discount / 100))
price_cleaner_discount = (quantity_cleaner * cleaner_amount) - (quantity_cleaner * cleaner_amount * (percentage_discount / 100))

total = price_pens_discount + price_marks_discount + price_cleaner_discount

print(total)
