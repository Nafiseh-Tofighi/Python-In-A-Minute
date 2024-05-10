"""
File: 009-AllAboutPrint()-Python_In_A_Minute.py
Author: Nafiseh J.Tofighi
Date: 10May2024

Description:
This script combines various usage examples of the print() function with different parameters such as 'sep', 'end', 'flush', and redirection to a file.

Usage:
- Run the script to see examples of different print() function usages.
"""


print("Hello, world!")

name = "Python"
age = 32
print("My name is", name, "and I am", age, "years old.")

# SEP
print('a','b','c')
#output: a b c

print('a','b','c', sep='')
#output: abc


print('a','b','c', sep='-')
#output: a-b-c


# END 
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

#FLUSH

import time

print('Start with flush')
for i in range(10):
  print('*', end=' ', flush=True)
  time.sleep(0.5)
print('\nDone')

#output: Start with flush
# * * * * * * * * * * 
# Done


print('Start without flush')
for i in range(10):
  print('*', end=' ', flush=False)
  time.sleep(0.5)
print('\nDone')

#output: Start without flush
# * * * * * * * * * * 
# Done


#FILE
# Open a file in write mode
with open("output.txt", "w") as f:
    # Redirect output to the file
    print("This is redirected output.", file=f)
    print("Hello, World!", file=f)
    print("Python is awesome!", file=f)
