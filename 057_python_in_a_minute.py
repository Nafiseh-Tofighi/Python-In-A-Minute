# -*- coding: utf-8 -*-
"""057-Python in a minute.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-OoAS5yPXWzmw3UCEauyCViz966FxyEC
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

# Convert all characters to lowercase
text = "Hello, World!"
result = text.lower()
print(result)  # Output: hello, world!

# String with uppercase letters
text = "PYTHON"
result = text.lower()
print(result)  # Output: python

# String with mixed case letters and special characters
text = "Python 3.8!"
result = text.lower()
print(result)  # Output: python 3.8!