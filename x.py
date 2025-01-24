# print("Hello, Word!")

# print("Hello Word")
# print("welcome to python")
# print ("have a great day")

# print("Hello, World!\nWelcome to Python programming.\nHave a great day!")
 
# x = "Hello"
# y = "word"
# print(x+""+y)

# x = "Hello"
# y = "word"
# print(x,y)

# x = "hello"
# y = "How"
# z = "you"

# print(x,y,z, sep="$")

# #  Print two messages on the same line using the end parameter.
# print("hello", end="")
# print("Word")

# print("hello", end="++")
# print("Word")

# # Print a message with quotes around it

# print ("Python, is great language")
# print ("Python, \"is great language\"")

# # Print the result of a Boolean expression.

# print(7>4)
# print(6<4)
# print (True and False)
# print (False and False)
# print (False and False)


# # Convert an integer to a float.

# x = 10
# print(x,type(x))

# x = 5
# y = float(x)
# print(y)
# print(type(y))

# # Q2: Convert a float to an integer.

# x = 5.7
# y = int(x)
# print(y)
# print(type(y))

# # Q3: Convert a string to an integer.

# x = "32"
# y = int(x)
# print(y)

# # Q4: Convert a string to a float.

# z = "23"
# k = float(z)
# print(k)
# print(type(k))

# #  Q5: Convert an integer to a string.

# x = 21
# y = str(x)
# print(y)
# print(type(y))

# # Q6: Convert a float to a string

# x = 8.9
# y = str(x)
# print(y)
# print(type(y))

# # Convert a binary string to an integer.

# x = "1010"
# y = int(x)
# print(y)
# print(type(y))

# x = "1010"
# y = int(x, 2)
# print(y)
# print(type(y))

# #3. Operators  
# # Q1. Create a program that takes two numbers as input and prints their sum.

# x = 100
# y = 100

# print(x+y)

# result_add = 5 + 3
# print("Addition:", result_add)

# #  Write a program that subtracts the second number from the first. Take these two numbers as input.

# x = 9-4
# print("subtracts:", x)

# # .Create a program that multiplies two numbers taken as input.

# x = 7* 4
# print("multiplies", x)

# #Q4. Write a program that divides the first number by the second (non-zero) number. Take these two numbers as input.

# x = 6/2
# print("divides", x)

# # Q5. Create a program that performs floor division on two numbers. Take these two numbers as input.

# x = 8//3
# print("floor division:", x)

# x = 10//2
# print("floor division:", x)

# # Q6. Write a program that calculates the remainder when the first number is divided by the second (non-zero) number. Take these two numbers as input.

# x = 40 % 9
# print("divided:", x)

# # Q7.Create a program that calculates the result of raising the first number to the power of the second number. Take these two numbers as input

# x = 4**4
# print(x)

# Q8.Write a program that calculates compound interest. Take the principal amount, rate of interest, and time as input.

# Q9.Create a program that takes a number as input, increments it, and then decrements it. Print both the incremental an
 
# Taking user input


# # Q10.Write a program that takes three numbers as input and calculates their average.
 
# # 2.Comparison Operator:
# # Q1.Write a program to compare two numbers and print whether they are equal or not.

# equal = 3==3
# print("equal:", equal)

# # not equal
# equal = 9 !=3
# print("not equal:", not equal)

# # Q2.Create a program that checks whether a given number is positive, negative, or zero.

# x = 3+6
# y = 3-6
# z = 8-8
# print(x,y,z)

# x = int(input('enter any number: '))
# y = int(input('enter any number: '))
# z = int(input('enter any number: '))
 
# if (x>y) and (x>z):
#     print('x any number: ')
# elif (y<x) and (y>z):
#     print('y any number: ')
# elif (z<x) :
#     print('z any number: ')
# else:
#     print('moduals')


# r = 20
# s = 40
# a =15

# if r<s and r<a:
#     print("ram")
# elif s>r and s<a:
#     print("shyam")
# else:
#     print("ajay")

# Given marks
# m1 = 70
# m2 = 50
# m3 = 80

# # Calculate percentage
# total_marks = m1 + m2 + m3
# percentage = (total_marks / 300) * 100  # Assuming each subject is out of 100

# # Assign grade based on percentage
# if percentage > 80:
#     grade = "A"
# elif 65 <= percentage <= 80:
#     grade = "B"
# elif 45 <= percentage < 65:
#     grade = "C"
# else:
#     grade = "D"

# Given year
# year = 2024

# # Check if the year is a leap year
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print("leap")
# else:
#     print("nonleap")



# print('------ 1.Function Returning Another Function ------')
# def create_machine():
#     def machine():
    
#         return("Machine Designed")
    
#     print('Machine Blueprint')
    

# design = create_machine()
# print(design)

# print()


# def show(x,y,z=100):
#     print(x,y,z)

# show(100,200,100)


