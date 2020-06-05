try:
    bill_amount = float(input("How much was the bill?\n"))
except ValueError:
    print('You did not give a valid number.')
    exit()

service_level = input("How was the service? Good, Fair, Bad\n")
tip = 0
if service_level == "Good":
    tip = bill_amount*.2
elif service_level == "Fair":
    tip = bill_amount*.15
elif service_level == "Bad":
    tip = bill_amount*.10
else:
    tip = float(input("Please enter specific amount:\n"))

print("Tip Amount: %s" % tip)
print("Total Amount: %s :" % (bill_amount + tip))

#using f function
# print(f"Tip Amount:{tip}")
# print(f"Total Amount: {bill_amount + tip}")