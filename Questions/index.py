# 1 Write a Python program to print "Hello Python"
a="hello python"
print(a)

#2  Write a Python program to do arithmetical operations addition and division.
#for additional
a=int(input("enter a first number"))
b=int(input("enter a second number"))
sum=a+b
print("the sum of numbers is", sum)

#for division
a=int(input("enter a first number"))
b=int(input("enter a sceond number"))
result=a/b
print("the divison of two number is : " , result)

#Program 3:Write a Python program to find the area of a triangle
height=int(input("enter a height of triangle"))
base=int(input("enter a base of triangle"))
result=height*base*0.5
print(" area of triangle" , result) 

# Program 4 : Write a Python program to swap two variables.
a=int(input("enter a first number"))
b=int(input("enter a second number"))
c=a
a=b
b=c
print("the value of a is:",a)
print("the value of b is:",b)

# Program 5  Write a Python program to generate a random number
import random
print("Random number:",{random.randint(1,100)})

#Program 6 Write a Python program to convert kilometers to miles.
kilometers=float(input("enter kilometer"))
conversion_factor = 0.621371
miles=kilometers*conversion_factor
print("the miles are:" , miles)

# Program 7 Write a Python program to convert Celsius to Fahrenheit
celsius=float(input("enter a temperature in  celsius"))
fahrenheit=(celsius*9/5)+32
print("temperature in fahrenheit" , fahrenheit)

#  Program 8 Write a Python program to display calendar.