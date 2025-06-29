# a = 2
# b = 5
# # here a and b are two variables.

# # Arithematic Operators
# # Add (+) 
# print("a + b =", a + b) #7
# # Subtract (-)
# print("a - b =", a - b) #-3
# # Multiply (*)
# print("a * b =", a * b) #10
# # Divide (/)
# print("a / b =", a / b) #0.4
# # Modulus (%)
# print("a % b =", a % b) #2
# # Exponentiation (**)
# print("a ** b =", a ** b) #32


# # Comparison Operators
# # Equal to (==)
# print("a == b:", a == b) #False
# # Not equal to (!=)
# print("a != b:", a != b) #True
# # Greater than (>)  
# print("a > b:", a > b) #False
# # Less than (<)
# print("a < b:", a < b) #True
# # Greater than equal to (>=)
# print("a >= b:", a >= b) #False
# # Less than equal to (<=)
# print("a <= b:", a <= b) #True

# #Assignment Operators
# # Assign (=)
# x = 10
# print("x =", x) #10
# # Add and assign (+=)
# x += 5
# print("x :", x) #15
# # Subtract and assign (-=)
# x -= 3
# print("x :", x) #12
# # Multiply and assign (*=)
# x *= 2
# print("x :", x) #24
# # Divide and assign (/=)
# x /= 4
# print("x :", x) #6.0
# # Modulus and assign (%=)
# x %= 5
# print("x :", x) #1.0
# # Exponentiation and assign (**=)
# x **= 3
# print("x :", x) #1.0

# # Logical Operators
# # Logical AND (and)
# p = True
# q = False
# print("p and q:", p and q) #False
# # Logical OR (or)
# print("p or q:", p or q) #True
# # Logical NOT (not)
# print("not p:", not p) #False





# Q2 write a program to input two numbers and print their sum.
# first = int(input("Enter first number: "))
# second = int(input("Enter second number: "))
# sum = first + second
# print(sum)


# Q3 write a program to input side of a square and print its area.
# a = float(input("Enter side of square: "))
# area = a * a
# print("Area of square:", area)

# Q4 write a program to input two floating point numbers and print their average.
# a = float(input("enter 1st decimal number :"))
# b = float(input("enter 2nd decimal number :"))
# average = (a + b) / 2
# print("Average of the two numbers is:", average)


# Q5 write a program to input 2 int numbers a and b . print True if a is greater than b otherwise print False.
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# equation = a >= b 
# print("Is a greater than or equal to b?", equation)  # True if a >= b, otherwise False\

# Q6 write a program to input users first name and print its length.
# fname = input("Enter your first name: ")
# leng = len(fname)
# print("Length of your first name is:", leng)


# Q7 write a program to find occurence of $ in a string.
# str = "hello ye mai hu$ aur mai boht$ menhnga hu $ pure $86.2 ka"
# print("Dollar present in string :", str.count('$'))

# Q8 grade students on based of marks
# marks = int(input("Enter your marks: "))
# if (marks >= 90):
#     print("Grade A+")
# elif (marks >= 80): 
#     print("Grade A")
# elif(marks >= 70):
#     print("Grade B+")
# elif(marks >= 60):
#     print("Grade B")
# elif(marks >= 50):
#     print("Grade C")
# elif(marks >= 40):
#     print("Grade D")
# else:
#     print("Fail") 


# Q9 write a program to input age of user and print if user is eligible to vote or not and can drive or not.
# age = int(input("Enter your age: "))
# if (age >= 18):
#     print("You are eligible to vote and can drive a car also.")
# else:
#     print("You are not eligible to vote and cannot drive a car.")


# Q10 write a program to input a number and check if it is even or odd.
# num = int(input("enter a numer: "))
# if (num % 2 == 0):
#     print(num,"Number is even")
# else:
#     print(num,"Number is odd")


# Q11 WAP to find the largest of three numbers.
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))  
# num3 = int(input("Enter third number: "))
# if (num1 >= num2) and (num1 >= num3):
#     print(num1, "is the largest number.")
# elif (num2 >= num1) and (num2 >= num3):
#     print(num2, "is the largest number.")
# else:
#     print(num3, "is the largest number.")


# Q12 WAP to check if a no. is multiple of 7 or not.
# num = int(input("Enter a number: "))
# if (num % 7 == 0):
#     print(num, "is a multiple of 7.")
# else:
#     print(num, "is not a multiple of 7.")    