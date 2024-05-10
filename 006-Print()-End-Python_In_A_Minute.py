"""
File: 006-Print()-End-Python_In_A_Minute.py
Author: Nafiseh J.Tofighi
Date: 10May2024

Description:
This script demonstrates the usage of the 'end' parameter in the print() function to control the behavior of the end of the printed output.

Usage:
- Run the script to see examples of different 'end' parameter usages.
"""

print('a')
print('b')
print('c')

#output: a
#b
#c

print('a', end='')
print('b', end='')
print('c', end='')
#output: abc

print('Hello', end='!')
print('World', end='!')
#output: Hello!World!

def draw_tree(levels):
    for i in range(1, levels + 1):
        print(" " * (levels - i), end="")
        print("*" * (2*i - 1), end="\n")

    # Print the trunk
    trunk_width = levels // 2
    trunk_spaces = (2*levels - trunk_width) // 2
    for _ in range(trunk_width):
        print(" " * trunk_spaces, end="")
        print("*" * trunk_width, end="\n")

draw_tree(6)
#output:

#      *
#     ***
#    *****
#   *******
#  *********
# ***********
#     ***
#     ***
#     ***

