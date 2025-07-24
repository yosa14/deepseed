password= input("enter your password:")
lower_case=password.islower()
upper_case=password.isupper()
numeric=password.isdigit()
if lower_case :
    if  upper_case: 
        if numeric:
            print("password is strong")
    else:
        print("try again")
else:
    print("please try again!!")