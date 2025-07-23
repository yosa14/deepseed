#concartenation and interpolation(istring operations in python) 
first_name="tancha "
last_name="josephine"
#concartenation
full_name= first_name  + last_name

#interpolation

print(f"my fullnames are {full_name}")

laugh = "ha" * 7
print(laugh)

#length
message = "hello,python!"
print(len(message))

#string formatting
name = "alice"
age =30
score = 95.5

#method 1
print(f"hello ,{name}! you are {age} years")
print(f"your score is {score:.1f}%")

#method 2
print("hello, {}! you are {} years old.".format(name, age))

#method 3
print("hello, %s! you are %d years old."% (name,age))