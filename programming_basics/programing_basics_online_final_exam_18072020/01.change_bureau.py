bitcoin_count = int(input())
chinese_count = float(input())
comision = float(input())

bitcoin_price_lv = 1168
dollar_price_lv = 1.76
euro_price_lv = 1.95
chinese_price_dolar = 0.15

bitcoin_price_euro = bitcoin_price_lv / euro_price_lv
dollar_price_euro = dollar_price_lv / euro_price_lv
chinese_price_euro = dollar_price_euro * chinese_price_dolar

wallet = bitcoin_price_euro * bitcoin_count + chinese_price_euro * chinese_count

money = wallet - wallet * comision / 100

moneyf = "{:.2f}".format(money)

print(moneyf)
