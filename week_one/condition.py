name = "Carrie"

message = """
What is your name?
"""

name = input(message)

if(name == "Carrie"):
    print("You may enter.")
else:
    print("Get out!")


print("Please Enter Your Age:")

older_than_twentyone = 21
age_of_use = int(input())

if age_of_use >= older_than_twentyone:
    print("Welcome!")
else:
    print("Get out!")