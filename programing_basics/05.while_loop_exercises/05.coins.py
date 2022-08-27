charge = float(input())
total_coins = 0

while charge != 0:
    if charge // 2 > 0:
        current_charged_coins = round(charge // 2)
        total_coins += current_charged_coins
        charge = round(charge - current_charged_coins * 2, 2)
        if charge == 0:
            break
    if charge // 1 > 0:
        current_charged_coins = round(charge // 1)
        total_coins += current_charged_coins
        charge = round(charge - current_charged_coins, 2)
        if charge == 0:
            break
    if charge // 0.5 > 0:
        current_charged_coins = round(charge // 0.5)
        total_coins += current_charged_coins
        charge = round(charge - current_charged_coins * 0.5, 2)
        if charge == 0:
            break
    if charge // 0.2 > 0:
        current_charged_coins = round(charge // 0.2)
        total_coins += current_charged_coins
        charge = round(charge - current_charged_coins * 0.2, 2)
        if charge == 0:
            break
    if charge // 0.1 > 0:
        current_charged_coins = round(charge // 0.1)
        total_coins += current_charged_coins
        charge = round(charge - current_charged_coins * 0.1, 2)
        if charge == 0:
            break
    if charge // 0.05 > 0:
        current_charged_coins = round(charge // 0.05)
        total_coins += current_charged_coins
        charge = round(charge - current_charged_coins * 0.05, 2)
        if charge == 0:
            break
    if charge // 0.02 > 0:
        current_charged_coins = round(charge // 0.02)
        total_coins += current_charged_coins
        charge = round(charge - current_charged_coins * 0.02, 2)
        if charge == 0:
            break
    if charge // 0.01 > 0:
        current_charged_coins = round(charge // 0.01)
        total_coins += current_charged_coins
        charge = round(charge - current_charged_coins * 0.01, 2)
        if charge == 0:
            break
total_coins = int(total_coins)

print(total_coins)
