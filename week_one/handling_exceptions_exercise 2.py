try:
    first_num = int(input("Number 1\n"))
    second_num = int(input("Number 2\n"))
    print ("The result is %s." % (first_num/second_num))
except ValueError:
    print('You input text')
    exit()

except ZeroDivisionError:
    print('You divided by zero')
    exit()



