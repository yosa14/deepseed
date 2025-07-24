# # # # #concartenation and interpolation(istring operations in python) 
# # # # first_name="tancha "
# # # # last_name="josephine"
# # # # #concartenation
# # # # full_name= first_name  + last_name

# # # # #interpolation

# # # # print(f"my fullnames are {full_name}")

# # # # laugh = "ha" * 7
# # # # print(laugh)

# # # # #length
# # # # message = "hello,python!"
# # # # print(len(message))

# # # # #string formatting
# # # # name = "alice"
# # # # age =30
# # # # score = 95.5

# # # # #method 1
# # # # print(f"hello ,{name}! you are {age} years")
# # # # print(f"your score is {score:.1f}%")

# # # # #method 2
# # # # print("hello, {}! you are {} years old.".format(name, age))

# # # # #method 3
# # # # print("hello, %s! you are %d years old."% (name,age))

# # # email = "user@example.com"
# # # if "@" in email and "." in email:
# # #    username = email.split("@")[0]
# # #    domain = email.split("@")[1]
# # #    print(f"username: {username}")
# # #    print(f"domain: {domain}")
# # # else:
# # #    print("invalid email format")
 
# # # text = "the quick brown fox jumps over the lazy dog"
# # # print(f"text: {text}")
# # # print(f"length: {len(text)} characters")
# # # print(f"word: {len(text.split())} words")
# # # print(f"uppercase: {text.upper()}")
# # # print(f"title case: {text.title()}")
# # # print(f"contains 'fox': {'fox'in text}")

# age = input("whats ur age")
# weight =input("whats ur weight")

# age, weight = age, weight

# # print("a =", a)
# # print("b =", b)

full_name ="johN dOe"
j=full_name[0].upper
N=full_name[3].lower
print(f"letter j:{j} N:[N]")

