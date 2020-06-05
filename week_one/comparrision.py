anakin_mc_count = 20421
yoda_mc_count = 19632
c3po_mc_count = 0

print(anakin_mc_count > 20000)
print(anakin_mc_count < yoda_mc_count)

print(anakin_mc_count >= 1000)

# greater than, less than, or greater/less than equal to

print(0 == c3po_mc_count)
# order does not matter - so 0 or c3po_mc_count can flip flop

print(c3po_mc_count != 10)
# != - not equal to, == equal t0

#conditions

# if it states true it is always true
name = 'Yoda'
if True:
    name = 'Yoda'
#the indention is a code block and will not print anything out of it
#to print anything else do not use indention
if False:
    name = 'Jar Jar Binks'

print("%s knows how to use a lightsaber" % name)

###
stars_wars_name = None
#none is always a false statement
message = """
Greetings:
Please enter Galactic ID Username
"""

stars_wars_name = input(message)

if(stars_wars_name != ""):
    print("Welcome %s your ID has been accepted." % stars_wars_name)
else:
    print("You must enter an ID to proceed!")

print("End of Transmission >>>")
#if a value = empty string = false
# "" , (), [], {}