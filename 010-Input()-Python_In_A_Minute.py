"""
File: 010-Input()-Python_In_A_Minute.py
Author: Nafiseh J.Tofighi
Date: 10May2024

Description:
This script demonstrates the usage of the input() function to receive user input in Python.

Usage:
- Run the script and input your age when prompted.
- Optionally, input your age directly after the prompt.
- Input your name when prompted and observe the greeting.
"""

age = input()

print(age)

age = input("Enter your age: ")

print('you are', age, 'years old.')

print('Hello', input('what is your name? '))
# output:
# what is your name? python
# Hello python

