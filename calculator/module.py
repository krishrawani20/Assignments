'''Assignment 1: Creating and Using a Simple Module
Task
1.
Create a module named calculator.py.
2.
Define functions:
▪
add(a,b)
▪
subtract(a,b)
▪
multiply(a,b)
▪
divide(a,b)
3.
Import the module into another program.
4.
Perform all four operations.'''
import calculator

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Addition:", calculator.add(a, b))
print("Subtraction:", calculator.subtract(a, b))
print("Multiplication:", calculator.multiply(a, b))
print("Division:", calculator.divide(a, b))