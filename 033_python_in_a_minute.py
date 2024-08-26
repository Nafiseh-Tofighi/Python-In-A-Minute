# -*- coding: utf-8 -*-
"""033-Python in a minute.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ktnff-CNCa1wD92adVdI9KGXBV8XyBKz
"""

# Code Example 1: Basic Usage
my_string = "Hello"
print(my_string.center(10))  # Output: "  Hello   "

# Code Example 2: Custom Fill Character
my_string = "Hello"
print(my_string.center(10, '-'))  # Output: "--Hello---

# Code Example 3: Centering with Larger Width
my_string = "Python"
print(my_string.center(20, '*'))  # Output: "*******Python*******"