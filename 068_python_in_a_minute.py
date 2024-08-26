# -*- coding: utf-8 -*-
"""068-Python in a minute.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1155uLEjGd-49TihK9LJHrtZaex93I0KU
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

# Simple split using whitespace
text = "hello world hello"
result = text.split()
print(result)  # Output: ['hello', 'world', 'hello']

# Split with specified separator
text = "apple,banana,cherry"
result = text.split(',')
print(result)  # Output: ['apple', 'banana', 'cherry']

# Split with maxsplit parameter
text = "apple,banana,cherry"
result = text.split(',', 1)
print(result)  # Output: ['apple', 'banana,cherry']