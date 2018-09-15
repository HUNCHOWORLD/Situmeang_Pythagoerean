"""
write a program that will ask the user to enter their name 
and respond with a greeting using there name
"""
from math import sqrt
print (" Hello! Welcome! ")

       
name = raw_input ("what is your name? ")
 
print ("Hello " + name + "!")

#lengths for pythagorean T

a = float(input("Please input side a: "))

b = float(input("Please inpute side b: "))

c = sqrt( a**2 + b**2)

hyp = sqrt (c)

print("The hypotenuse of a right angled triangle with side a =",a,"and side b =",b,"equals ",hyp )