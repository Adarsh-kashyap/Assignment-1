# Assignment_1
# Task_1---------> Perform Basic Mathematical Operations
'''
Problem Statement: Write a Python program that does the following:
1.Takes two numbers as input from the user.
2.Performs the basic mathematical operations on these two numbers:
3.Addition
4.Subtraction
5.Multiplication
6.Division
7.Displays the results of each operation on the screen.
'''
A=input('Enter the first number: ')
B=input('Enter the second number: ')
A=float(A)
B=float(B)
Addition=A+B
Subtraction=A-B
Multiplication=A*B
if B!= 0:
    Division= A/B
else:
    Division="Undefined (division by zero)"
print('Addition: ', Addition)
print('Subtraction: ', Subtraction)
print('Multiplication: ', Multiplication)
print('Division: ', Division)

#Task_2------>Create a Personalized Greeting
'''
Problem Statement: Write a Python program that:
1.  Takes a user's first name and last name as input.
2.  Concatenates the first name and last name into a full name.
3.  Prints a personalized greeting message using the full name.
'''
A=input('Enter your first name: ')
B=input('Enter your last name: ')
A=str(A)
B=str(B)
C=A +" " + B
print("Hello, " + C + "! Welcome to the Python Program")
