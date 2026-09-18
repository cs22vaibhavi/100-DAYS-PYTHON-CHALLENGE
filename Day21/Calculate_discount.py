def calculate_discount(price, discount):
    amount = price * discount / 100
    return price - amount

final_price = calculate_discount(1000, 10)

print("Final Price =", final_price)
