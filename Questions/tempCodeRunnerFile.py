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