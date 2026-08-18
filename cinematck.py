# Cinema Ticket Bill Calculation using Arithmetic Operators

ticket_price = 250
tickets = 4
discount = 100

total_bill = ticket_price * tickets

if total_bill > 500:
    final_amount = total_bill - discount
else:
    final_amount = total_bill

print("Ticket Price:", ticket_price)
print("Number of Tickets:", tickets)
print("Total Bill:", total_bill)
print("Discount:", discount)
print("Final Amount Payable:", final_amount)