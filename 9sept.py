
a = "hello world "
b = "abcdefghij "
c = "uhdsfhjsdjh"
d = 10
e = 20

#slicing
# print(a[2:5])  
# print(a[0:5])  
# print(a[:5])   
# print(a[2:])   
# print(a[-5:-2])  
# print(a[-5:])   
# print(a[:-2])   
# print(a[:])     
# print(a[-5:-2]) 
# print(a[-5:])    

#methods
print(a.replace("l", "j"))
print(a.split("o"))
print(a.upper())
print(a.lower())
print(a.capitalize())
print(len(a))

#concatenation
print("b + c =", b + c)
  
# format method 
# it formats the specify values and insert them inside the string's placeholder.
#placeholder can be identified using index number, index name, or empty.
print("the {} {} {}".format(a, b, c))
print("the {2} {1} {0}".format(a, b, c))
print("the {x} {y} {z}".format(x=a, y=b, z=c))

# f string
print(f"the {a} {b} {c}")
print(f"the {a} {b} {c} {d} {e} {d+e}")
print(f"the {a} {b} {c} {d} {e} {d*e}")


# operators
a = 2
b = 5
# here a and b are two variables.

# Arithematic Operators
# Add (+) 
print("a + b =", a + b) #7
# Subtract (-)
print("a - b =", a - b) #-3
# Multiply (*)
print("a * b =", a * b) #10
# Divide (/)
print("a / b =", a / b) #0.4
# Modulus (%)
print("a % b =", a % b) #2
# Exponentiation (**)
print("a ** b =", a ** b) #32


# Comparison Operators
# Equal to (==)
print("a == b:", a == b) #False
# Not equal to (!=)
print("a != b:", a != b) #True
# Greater than (>)  
print("a > b:", a > b) #False
# Less than (<)
print("a < b:", a < b) #True
# Greater than equal to (>=)
print("a >= b:", a >= b) #False
# Less than equal to (<=)
print("a <= b:", a <= b) #True

#Assignment Operators
# Assign (=)
x = 10
print("x =", x) #10
# Add and assign (+=)
x += 5
print("x :", x) #15
# Subtract and assign (-=)
x -= 3
print("x :", x) #12
# Multiply and assign (*=)
x *= 2
print("x :", x) #24
# Divide and assign (/=)
x /= 4
print("x :", x) #6.0
# Modulus and assign (%=)
x %= 5
print("x :", x) #1.0
# Exponentiation and assign (**=)
x **= 3
print("x :", x) #1.0

# Logical Operators
# Logical AND (and)
p = True
q = False
print("p and q:", p and q) #False
# Logical OR (or)
print("p or q:", p or q) #True
# Logical NOT (not)
print("not p:", not p) #False
print("not q:", not q) #True

# membership operators
# Membership in (in)
print("'h' in a:", 'h' in a) #True
print("'z' in a:", 'z' in a) #False
# Membership not in (not in)
print("'h' not in a:", 'h' not in a) #False
print("'z' not in a:", 'z' not in a) #True

# Identity operators
# Identity is (is)
m = 5
n = 5
print("m is n:", m is n) #True
# Identity is not (is not)
n = 10
print("m is not n:", m is not n) #True

#Bitwise Operators
# Bitwise AND (&)
print("a & b =", a & b) #0
# Bitwise OR (|)
print("a | b =", a | b) #7
# Bitwise NOT (~)
print("~a =", ~a) #-3
# Bitwise XOR (^)
print("a ^ b =", a ^ b) #7
# Bitwise right shift (>>)
print("a >> 1 =", a >> 1) #1
# Bitwise left shift (<<)
print("a << 1 =", a << 1) #4

