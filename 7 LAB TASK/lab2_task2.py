# lab2_task2.py

def calculate_price(price, tax_rate=18, discount=0):
    price_after_discount = price - (price * discount / 100)
    final_price = price_after_discount + (price_after_discount * tax_rate / 100)
    return final_price

print(f"(a) Only price ($100): ${calculate_price(100):.2f}")
print(f"(b) Price ($100) + custom tax (12%): ${calculate_price(100, 12):.2f}")
print(f"(c) All overridden ($100, tax 12%, disc 10%): ${calculate_price(100, 12, 10):.2f}")

OUTPUT:
# (a) Only price ($100): $118.00
# (b) Price ($100) + custom tax (12%): $112.00
# (c) All overridden ($100, tax 12%, disc 10%): $100.80
