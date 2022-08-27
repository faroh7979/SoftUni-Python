company_name = input()
adult_num_tickets = int(input())
children_num_tickets = int(input())
net_price_adult = float(input())
cs_tax = float(input())

net_price_children = net_price_adult * 0.3
cs_tax_total = (adult_num_tickets + children_num_tickets) * cs_tax
all_tickets_price = (adult_num_tickets * net_price_adult) + (children_num_tickets * net_price_children)

total_ticket_price = cs_tax_total + all_tickets_price

profit = total_ticket_price * 0.2
profit_format = "{:.2f}".format(profit)

print(f"The profit of your agency from {company_name} tickets is {profit_format} lv.")
