number = 1
while number <= 10:
    seperater ='\n-----'
    print("%s" % number, seperater)
    number += 1


number = 100 
seperater ='\n-----'
while number >= 0:
    if number != 50 and number != 30:
        print(f'Downloand remaining: {number}%', seperater)
    number -= 10
    
number = 100
dec_by = 10
while number >= 0:
    if number != 50 and number != 30:
         print('%s%% downloaded %s%% remaining.' % (100-number, number))
    number -= dec_by
