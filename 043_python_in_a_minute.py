# -*- coding: utf-8 -*-
"""043-Python in a minute.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1QwaqkYvyYeEy43Fgjsvwyf6gHQnFazR1
"""

from IPython.display import HTML
shell = get_ipython()

def adjust_font_size():
  display(HTML('''<style>
    body {
      font-size: 28px;
    }
  '''))

if adjust_font_size not in shell.events.callbacks['pre_execute']:
  shell.events.register('pre_execute', adjust_font_size)

# Sample strings
text1 = "Python"

# Checking if the string is alphabetic
print(text1.isalpha())  # Output: True

# Sample strings
text2 = "Python3"

# Checking if the string is alphabetic
print(text2.isalpha())  # Output: False

# Sample strings
text3 = "HelloWorld"

# Checking if the string is alphabetic
print(text3.isalpha())  # Output: True

# Sample strings
text4 = "Hello World"

# Checking if the string is alphabetic
print(text4.isalpha())  # Output: False