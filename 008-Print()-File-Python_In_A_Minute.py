"""
File: 008-Print()-File-Python_In_A_Minute.py
Author: Nafiseh J.Tofighi
Date: 10May2024

Description:
This script demonstrates how to redirect output from the print() function to a file using the 'file' parameter.

Usage:
- Run the script to see examples of redirecting output to a file.
"""

# Open a file in write mode
with open("output.txt", "w") as f:
    # Redirect output to the file
    print("This is redirected output.", file=f)
    print("Hello, World!", file=f)
    print("Python is awesome!", file=f)
