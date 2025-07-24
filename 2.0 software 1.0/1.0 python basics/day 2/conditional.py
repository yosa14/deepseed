# # # # #  if age is more than 18 can vote else can't vote
# # # # age=int(input("please enter your age:"))
# # # # if (age) > 18:
# # # #     print("yes you can vote")
# # # #else:
# # #  #    print("please wait for next year elections")

# # # age=int(input("how old are you: "))
# # # if age > 16:
# # #     print("yes cam play basketball")
# # # else:
# # #     print("cant play")

# #grade management system

# # grade=int(input("enter marks: "))
# # if grade >= 80:
# #     print("A grade")
# # elif grade >= 70 < 80:
# #     print("B+ grade")
# # elif grade  >= 60 < 80:
# #     print("B grade")
# # elif grade >= 50 < 60:
# #     print("C grade")
# # elif grade >= 40 < 50:
# #     print("D grade")
# # else:
# #     print("very poor😭😭😭😭😭😭😭😭😭😭😭😭")


# #simple calculator
# first_number=float(input("enter first number: "))
# second_number=float(input("enter second number: "))
# operator=input("Enter operator")
# result=0

# if operator=="+":
#     result=first_number + second_number
#     print(F" answer is: {result}")
# elif operator=="*":
#     result=first_number * second_number
#     print(F" answer is: {result}")
# elif operator=="-":
#     result=first_number - second_number
#     print(F" answer is: {result}")
# elif operator=="/":
#     if second_number!=0:
#         result=first_number / second_number
#         print(F" answer is: {result}")
# else: 
#     print(f"second number should not be zero")

# leap year
year=int(input("enter year: "))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("its leap a year")
        else:
            print("not a leep year")    
    else:
        print("is a leap yer")
else:
    print(" not a leap year")