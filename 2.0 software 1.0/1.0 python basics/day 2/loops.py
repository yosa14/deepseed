# # # # # # # # # # # for loop
# # # # # # # # # # # 1.starting point
# # # # # # # # # # # 2. condition
# # # # # # # # # # # 3. increment or dicrement
# # # # # # # # # # names=["will","loe","kate","kilian" ,"fgbom","rtybom"]
# # # # # # # # # # print(names[0])
# # # # # # # # # # print(names[1])
# # # # # # # # # # print(names[2])
# # # # # # # # # # print(names[3])

# # # # # # # # # # for name in names:
# # # # # # # # # #     print(name)
# # # # # # # # # #     if name.endswith("bom"):
# # # # # # # # # #         print(f"we don catch u: {name}")
# # # # # # # # # #     else:
# # # # # # # # # #          print(f"welcome to the party : {name}")

# # # # # # # # # # count=1
# # # # # # # # # # for name in names:
# # # # # # # # # #     print(f"{count}. {name}")
# # # # # # # # # #     count = count + 1

# # # # # # # # # my_names="Josephine"
# # # # # # # # # for letter in my_names:
# # # # # # # # #     print(f"letter: {letter}")
 
# # # # # # # # range method in looping
# # # # # # # #range stop starts from o
# # # # # # # #for i in range(5):
# # # # # # # #    print(i)

# # # # # # #range(start, stop)
# # # # # # # for i in range(2,7):
# # # # # # #     print(i)

# # # # # # #range(start, stop, step)
# # # # # # for i in range(0, 10, 2):
# # # # # #     print(i)

# # # # # #count down
# # # # # for i in range(10, 0, -1):
# # # # #     print(f"countdown: {i}")
# # # # # print("HAPPY BIRTHDAY✈️")
# # # # while True:
# # # #     print("madness")

# # # #basic while loop

# # # count = 1
# # # while count <= 5:
# # #     print(f"count is: {count}")
# # #     count += 1

# # # #user input loop 
# # # user_input = ""
# # # while user_input != "quit":
# # #     user_input = input(" enter 'quit' to exit ")
# # #     if user_input != "quit":
# # #         print(f"you entered: {user_input}")


# # # print("dont go😭😭😭😭😭")

# # # break exit the loop completely
# # print("finding the first even number:")
# # for number in range(1, 10):
# #     if number % 2 ==0:
# #         print(f"found even number: {number}")
# #         break
# #     print(f"{number} is odd")

# # #continue - skip to next iteration
# # print("\nprinting only odd numbers:")
# # for number in range(1, 10):
# #     if number % 2 == 0:
# #         continue
# #     print(f"0dd number: {number}")

# #nested loops
# #multiplication table
# print("Multiplication Table:")
# for i in range(1, 4):
#     for j in range (1, 4):
#         result = i * j
#         print(f"{i} x {j} = {result}")
#     print()

#pattern printing
print("triangle pattern:")
for row in range(1, 6):
    for star in range(row):
        print("*", end=" ")
    print()