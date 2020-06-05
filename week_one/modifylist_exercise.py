# number = None
# numbers = []
# #this creates a empty list
# result = 0

# while number != 0:
#     number = int(input("Please give me a number to add (Pressing 0 will do the addition: "))
#     numbers.append(number)
#     #taking numbers list and add number
#     print(numbers)

# result = sum(numbers)
# print(result)


#below is with challenge:

number = None
numbers = []
result = 0

while number != 0:
    try:
        number = int(input("Please give me a number to add (Pressing 0 will do the addition: "))
    except ValueError:
        print('You must give a valid number!')
        number = None
   
    numbers.append(number)
    #taking numbers list and add number
    
    if number == None:
        numbers.pop()
    print(numbers)

result = sum(numbers)
print(result)