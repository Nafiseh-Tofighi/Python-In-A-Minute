# -*- coding: utf-8 -*-
"""050-Python in a minute.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/17WxSPT3OLV8qN7CRFNOyBOPj6h-mE-OP
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

"""**isdecimal()** --> decimal characters(numbers in base 10)

**isdigit()** --> decimal characters and superscript numbers

**isnumeric()** --> digits, fractions, Roman numerals

"""

# String with decimal characters
text = "12345"
print(text.isdecimal())  # Output: True
print(text.isdigit())    # Output: True
print(text.isnumeric())  # Output: True

# String with superscript numbers
text = "²³⁴"
print(text.isdecimal())  # Output: False
print(text.isdigit())    # Output: True
print(text.isnumeric())  # Output: True

# String with a fraction
text = "⅓"
print(text.isdecimal())  # Output: False
print(text.isdigit())    # Output: False
print(text.isnumeric())  # Output: True

