# -*- coding: utf-8 -*-
"""071-Python in a minute.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10WiIgZ53MxlLopZ_P-17Cy8bhGBtmnOR
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

# Simple split at line breaks
text = "hello\nworld\nhello"
result = text.splitlines()
print(result)  # Output: ['hello', 'world', 'hello']

# Split at line breaks with keepends parameter
text = "hello\nworld\nhello"
result = text.splitlines(True)
print(result)  # Output: ['hello\n', 'world\n', 'hello']

# Comparing with split() method
text = "hello\nworld\nhello"

result = text.splitlines()
print(result)  # Output: ['hello', 'world', 'hello']

result = text.split('\n')
print(result)  # Output: ['hello', 'world', 'hello']