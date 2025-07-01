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


# list 
# num = [1, 25, 4, 45, 7, 18, 10]
# num.append(12)
# print("List after appending 12:", num)
# num.insert(2, 100)
# print("List after inserting 100 at index 2:", num)
# num.reverse()
# print("List after reverse: ",num)
# num.sort()
# print("List after sorting: ", num)
# num.remove(100)
# print("List after removing 100:", num)
# num.pop(4)
# print("List after POP: ",num)

#Tuples
# tup = (1, 4, 6, 7, 1, 7, 2, 4)
# print(type(tup))
# print("index of first occurence: ",tup.index(6))
# print("total occurence: ",tup.count(4))

# Q13 WAP to ask the user to enter names of their 3 favoraite movies and store them in a list.
# movies = []
# movie1 = input("Enter First Movie: ")
# movie2 = input("Enter Second Movie: ")
# movie3 = input("Enter Third Movie: ")

# movies.append(movie1)
# movies.append(movie2)
# movies.append(movie3)
# print("Your favorite movies are:", movies)

# Q14 WAP to check if a list contain a palindrome of element.
# num = [1, 2, 3, 4, 8, 4, 3, 2, 1]
# cnum = num.copy()
# cnum.reverse()
# if (num == cnum):
#     print("List is a palindrome.")
# else:
#     print("List is not a palindrome.")

# Q15 WAP to count the numbers of student with the "A" grade in a tuple.
# grades = ('A', 'B', 'A', 'C', 'A', 'B', 'A')
# print("Total number of students with grade 'A':", grades.count('A'))

# Q16 WAP to sory the following list in ascending order.
# Alphabets = ['A', 'B', 'A', 'C', 'A', 'B', 'A']
# Alphabets.sort()
# print("Original list:", Alphabets)



# #Dictionary
# student = {
#     "name": "Aditya saini",
#     "age": 20,
#     "subjects": { "Math": 89,
#                   "Science": 85,
#                   "English": 90 
#                   }
# }

# # methods in dictionary
# print(student.get("name"))
# print(list(student.keys()))
# print(list(student.values()))
# print(list(student.items()))
# student.update({"city": "Delhi"})
# print("Updated Student Dictionary:", student)

#Sets
# my_set = {1, 2, 3, 4, 5}
# my_set.add(6)
# print("Set after adding 6:", my_set)
# my_set.remove(3)
# print("Set after removing 3:", my_set)
# my_set.discard(10)  # No error if 10 is not present
# print("Set after discarding 10:", my_set)
# my_set.clear()
# print("Set after clearing:", my_set)
# my_set = {1, 2, 3, 4, 5}
# my_set2 = {4, 5, 6, 7, 8}
# union_set = my_set.union(my_set2)
# print("Union of sets:", union_set)
# intersection_set = my_set.intersection(my_set2)
# print("Intersection of sets:", intersection_set)

# Q17 store following word meanings in a dictionary.
# table : "list of items "
# cat: "a small domesticated carnivorous mammal"

# WORD_MEANINGS = {
#     "table": "list of items",
#     "cat": "a small domesticated carnivorous mammal"
# }
# print("Word Meanings Dictionary:", list(WORD_MEANINGS.items()))


# Q18 you are given a list of students assume one classroom is required for each subject. how many classrooms are required?
    # "python","java", "c++", "python", "javascript", "python", "c++", "java", "python", "c++", "c"
# set_of_subjects = {"python","java", "c++", "python", "javascript", "python", "c++", "java", "python", "c++", "c"}
# print("Number of classrooms required:", len(set_of_subjects))

# Q19 WAP to enter marks of 3 subject from the user and store them in a dictionary.start with empty dictionary and add one by one use subject name as key and marks as value.
# dictionary = {}
# physics = int(input("Enter marks of Physics: "))
# chemistry = int(input("Enter marks of Chemistry: "))
# maths = int(input("Enter marks of Maths: "))

# dictionary["Physics"] = physics
# dictionary["Chemistry"] = chemistry
# dictionary["Maths"] = maths
# print("Marks:", list(dictionary.items()))