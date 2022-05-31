ticket_a_price = int(19.99)
ticket_c_price = int(8.99)
booking_fee = int(2.50)

ticket_a_amount = int(input("How many adult tickets?"))
ticket_c_amount = int(input("How many child tickets?"))

total_a = ticket_a_amount*ticket_a_price
total_c = ticket_c_amount*ticket_c_price

g_total = total_a+total_c+booking_fee

print(g_total)





