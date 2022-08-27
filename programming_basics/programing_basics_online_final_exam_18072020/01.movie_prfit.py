movie_name = input()
days_count = int(input())
tickets_count = int(input())
ticket_price = float(input())
cinema_comision_percentage = int(input())

gross_profit = tickets_count * ticket_price * days_count
net_profit = gross_profit - gross_profit * cinema_comision_percentage / 100
net_profitf = "{:.2f}".format(net_profit)

print(f"The profit from the movie {movie_name} is {net_profitf} lv.")
