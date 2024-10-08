# -*- coding: utf-8 -*-
"""046-Python in a minute.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1J1brbkwfDKGZh4tT5tUyHTgm5aPBsS3e
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

# Check if all characters are digits
text = "12345"
print(text.isdigit())  # Output: True

# String with non-digit characters
text = "12345.0"
print(text.isdigit())  # Output: False

# String with superscript numbers
text = "⁰¹²³"
print(text.isdigit())  # Output: True

# Compare with isdecimal()
text = "⁰¹²³"
print(text.isdecimal())  # Output: False

