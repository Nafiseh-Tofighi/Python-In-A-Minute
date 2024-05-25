"""
File: 030-Strings-Slicing-Python_In_A_Minute.py
Author: Nafiseh J.Tofighi
Date: 25May2024

Description:
This script demonstrates different examples of string slicing in Python.

Usage:
- Explore basic slicing operations on strings using start, end, and step indices.
- Understand how negative indices work in slicing.
"""

# Example 1: Basic slicing -->   string[start:end:step]
s = 'Hello, World!'
print(s[0:5])  # Output: Hello

# Example 2: Using step in slicing
s = 'Hello, World!'
print(s[0:12:2])  # Output: Hlo ol

# Example 3: Omitting start and end indices
s = 'Hello, World!'
print(s[:5])   # Output: Hello
print(s[7:])   # Output: World!

# Example 4: Using negative indices
s = 'Hello, oWrld!'
print(s[-6:-1])  # Output: World

