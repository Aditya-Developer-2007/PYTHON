
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
