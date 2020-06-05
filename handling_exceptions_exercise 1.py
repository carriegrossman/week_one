#exercise 1
number = input("Enter a number between 10 and 101 \n")

try:
    number = int(number)
except ValueError:
    print('This is wrong.')
    exit()
#this exits a program or to completely stop
if number == -1:
    print("Very smart!")
elif number < 10 or number > 101:
    print('Try again.')
elif number == 42:
    print('Great!')
else:
    print('Perfect! %s was your number.' % number)
