#ex2
bill_amount = 0
while bill_amount == 0:
    try:
        bill_amount = float(input("How much was the bill?\n"))
    except ValueError:
        print('You did not give a valid number.')


service_level = input("How was the service? Good, Fair, Bad\n")
#tip = 0
tip = bill_amount*.2
if service_level == "good":
    tip = bill_amount*.2
elif service_level == "fair":
    tip = bill_amount*.15
elif service_level == "bad":
    tip = bill_amount*.10
else:
    print('Incorrect value given. Default to good')
total = bill_amount+tip
print("Tip Amount: %s" % tip)
print("Total Amount: %s" % (total))

try: 
    people = int(input("Split how many ways?\n"))
    if people == 0:
        people = 1
except ValueError:
    people = 1
    print('Invalid number. Assumes 1')

split_amount = total/people

print("This amount for each individual is: %s" % split_amount)