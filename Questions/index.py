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
import calendar
year=int(input("enter a year: "))
month=int(input("enter a month: "))
cal=calendar.month(year,month)
print(cal)

# Program 10  Write a Python program to swap two variables without temp variable
a=eval(input("enter a number "))
b=eval(input("enter a number"))
a,b=b,a
print("value of a is : ", a )
print("value of b is ",b)

#Program 11  Write a Python Program to Check if a Number is Positive, Negative or Zero
num=eval(input ("enter a number:"))
if num>0:
    print("number is positive")
elif num==0:
    print("the number is zero")
else: print("number is negative")

# Program 12 Write a Python Program to Check if a Number is Odd or Even.
num=eval(input("enter a number"))
if num%2==0:
    print("the number is even")
else :
    print("the number is odd")
    
#Write a program to check if a number is positive, negative, or zero.
num=int(input("enter a number : " ))
if num>0:
    print("no. is positive")
elif num<0:
    print("no.is negative ")
else :
    print("no.is zero ")
 
#Take user input and check if it is even or odd.
num=int(input("enter a number: "))
if num%2==0:
    print("the no.is even")
else :
    print("the no.is odd")    
 
#check if a year is a leap year or not.
year=int(input("enter a year"))
if year % 4 == 0  and year % 100!=0:
    print("year is leap year")
elif year % 400 == 0:
    print("is leap year")
else :
    print("year is not a leap year")    
    

 # Write a program to check if a person is eligible to vote.
age=int(input("enter age: "))
if age >=18:
     print("eligible to vote")  
else:
     print("not eligible to vote")    
     
# Write a program to find the greatest among two numbers.     
num1=int(input("enter a 1st number: "))
num2=int(input("enter a sec no:  "))
if num1>=num2:
    print("the 1st no. is greatest")
else:
    print(" the 2nd no. is greatest")    
 
 #Check if the given character is a vowel or a consonant.   
char=input("enter a single character: ")
if char in "aeiouAEIOU":
    print("it is a vowel")
    
else :
    print("it is consonant")    
    
#Write a program to find the greatest among three numbers.   
num1=int(input("enter a 1st no.:")) 
num2=int(input("enter a 2nd no.:")) 
num3=int(input("enter a 3rd no.:")) 
if num1>=num2 and num1>=num3:
    print("1st no. is greatest")
elif num2>=num1 and num2>=num3:
    print("2nd no. is greatest")
    
else: 
    print("3rd no. is greatest")

   
    
# Given a character, determine whether it is an uppercase letter, lowercase letter, digit, or special character.
char=input("enter a single char")
if len(char)!=1:
    print("please enter a single char ")
else:
    if char.islower():
        print('char is lowercase letter')  
        
    elif char.isupper():
        print("char is uppercase letter") 
    elif char.isdigit():
        print("it is digit")    
    else :
        print("it is special character ")             
        
        