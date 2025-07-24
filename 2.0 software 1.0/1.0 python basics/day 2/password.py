# password= input("enter your password: ")
# lower_case=password.islower()
# upper_case=password.isupper()
# numeric=password.isdigit()
# if lower_case :
#     if  upper_case: 
#         if numeric:
#             print("password is strong")
#     else:
#         print("try again")
# else:
#     print("please try again!!")
l=False
u = False
d=False
password = input("enter your password: ")
for letter in password:
    if letter.islower():
        l=True
    elif letter.isupper():
        u=True
    elif letter.isdigit():
        d = True
    
if l and u and d:
    print("strong password")
else:
    print("weak password")
