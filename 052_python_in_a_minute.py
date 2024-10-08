# -*- coding: utf-8 -*-
"""052-Python in a minute.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-n_oqNxQbeDNiIyRVN8iuPOroKhStU00
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

# Check if all characters are whitespace
text = "   "
print(text.isspace())  # Output: True

# String with non-whitespace characters
text = "   a   "
print(text.isspace())  # Output: False

# String with different types of whitespace characters
text = "\t\n "
print(text.isspace())  # Output: True