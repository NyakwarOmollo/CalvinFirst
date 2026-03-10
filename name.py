# Declaration
first= "Hello World"

#This is a comment

#Log message
print("I AM A COMPUTER!")

# AN if statement
if (1<2 and 4>2):
 print("Math is fun")

# Assignment
nope= None

# Using the boolean operator
result= True and False
print("True and false=",result)

#Length calculation
length= len("What's my length?" )
print("length of 'What's my length?",length)

#Conversion of string to number
number = int("1000")
print("Converted number:", number)         
print("Type:", type(number))   

#Conversion to uppercase
shouting = "i am shouting".upper()
print("Uppercase:", shouting)

#Combination of number 4 and "real"
combined = str(4) + "real"
print("Combined:", combined)

#output of expression of 3* "cool"
print("3 * 'cool' →", 3 * "cool")

#output of 1/0
try:
    result = 1 / 0
except ZeroDivisionError as e:
    print("1 / 0 → raises:", type(e).__name__)  
    print("Error message:", str(e))

#Determining the type of []
print("Type of []:", type([]))

#Asking a user for their name
name = input("What is your name? ")
print("Hello,", name)

#Ask the user for their name, and store it in a variable called name
name = input("What is your name? ")
print("Hello,", name)

#Ask the user for a number and give feedback
try:
    num = float(input("Enter a number: "))
    if num < 0:
        print("That number is less than 0!")
    elif num > 0:
        print("That number is greater than 0!")
    else:
        print("You picked 0!")
except ValueError:
    print("That's not a valid number!")

#Check whether a string called my_string is all in lowercase
my_string = "python is awesome"
is_lowercase = my_string.islower()
print("Is my_string all lowercase?", is_lowercase)   

# You can change my_string to test:
# my_string = "Python Is Awesome"
# print("Is my_string all lowercase?", my_string.islower())  
