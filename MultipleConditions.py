user_name = input("What is the username?\n")
password = input("What is the password?\n")

if len(user_name) < 6 or len(password) < 6:
    print('Your Username or Password is too short.')
elif len(user_name) > 12 or len(password) > 12:
    print('Your username or password is too long.')

confirm_password = input("Confirm Password\n")

if comfirm_password == pasword:
     if confirm_password.isdigit():
        print('Fail')
     else:
        print('Success!')

else:
    print('Fail')