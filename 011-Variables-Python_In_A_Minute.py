"""
File: 011-Variables-Assignment-Python_In_A_Minute.py
Author: Nafiseh J.Tofighi
Date: 10May2024

Description:
This script demonstrates variable assignment and reassignment in Python, as well as multiple variable assignment.

Usage:
- Run the script to see examples of variable assignment and multiple variable assignment.
"""

x= 22

print(x)
#output: 22

y='Hello, World!'

print(y)
#output: Hello, World!

print(type(x))
#output: <class 'int'>

print(type(y))
#output: <class 'str'>

x= 42

print(x)
#output: 42

x= y

print(x)
#output: Hello, World!

print(type(x))
#output: <class 'str'>

num1, num2, num3 = 5, 10, 15

print(num3, num2, num1)
#output: 15 10 5

a = b = c = 'Hello!'
print(a,b,c)
#output: Hello! Hello! Hello!

