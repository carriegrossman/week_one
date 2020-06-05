#secret_number = 5
import random
secret_number = random.randint(1, 10)

print("I am thinking of a number between 1 and 10.")
number = 0
num_guesses = 5
while number != secret_number:
    try:
        number = int(input("What's the number? "))
        if number != secret_number:
            num_guesses -= 1
            print("Nope, try again.")
            print("You have %s guesses left" % num_guesses)
            if number < secret_number:
                print("%s is too low." % number)
            elif number > secret_number:
                print("%s is too high." % number)
        elif number == secret_number:
            print("Yes! You win!")
    except ValueError:
        print('You did not give a valid number.')

