# lab2_task5.py

def order_summary(customer, *items, discount=0, **extra):
    print(f"Customer Name: {customer}")
    print(f"Ordered Items: {', '.join(items)}")
    print(f"Discount Applied: {discount}%")
    if extra:
        print("Extra Information:")
        for key, val in extra.items():
            print(f"  - {key}: {val}")

order_summary("Meera", "Laptop", "Mouse", discount=10, delivery_address="Hyderabad", gift_wrap=True)

OUTPUT:
# Customer Name: Meera
# Ordered Items: Laptop, Mouse
# Discount Applied: 10%
# Extra Information:
#   - delivery_address: Hyderabad
#   - gift_wrap: True
