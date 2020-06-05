my_num = 10
my_second_num = 5

#if you have a input put within the while "Like confirming a passowrd"

while my_num > 0:
    print("First number is %s" % my_num)
    my_num -= 2
    while my_second_num <= 20:
        print("Second num %s" % my_second_num)
        my_second_num += 5
    print('Done with nested loop')
    my_second_num = 5

print("This will print after the loop")