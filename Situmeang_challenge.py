from math import sqrt
print (" Hello! Welcome! ")

       
name = raw_input ("what is your name? ")
 
print ("Hello " + name + "!")

#lengths for pythagorean T

a = float(input("Please input side a: "))

b = float(input("Please input side b: "))

c = float(input("Please input side c: "))

ab = sqrt( a**2 + b**2 )

if (a+b < c):
     print(' This is not a triangle')
        
if (a**2 + b**2 == c**2):
    print (' This is a right triangle')
        
if (a**2 + b**2 < c**2):
    print (' This is an obuse triangle')
    
if (a**2 + b**2 > c**2):
    print (' This is an acute triangle')