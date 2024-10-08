# -*- coding: utf-8 -*-
"""087-Python in a minute.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1orpy2C_TlI8vZAev46IMcwYWZPKze0tE
"""

from IPython.display import HTML
shell = get_ipython()

def adjust_font_size():
  display(HTML('''<style>
    body {
      font-size: 20px;
    }
  '''))

if adjust_font_size not in shell.events.callbacks['pre_execute']:
  shell.events.register('pre_execute', adjust_font_size)

# Asterisk *:

# Pattern: ca*t

# Matches:
'ct'
'cat'
'caat'
'caaaaaat'
# Does not match:
'cbt'

# Plus sign +:

# Pattern: ca+t

# Matches:
'cat'
'caat'
'caaaaat'
# Does not match:
'ct'

# Question mark ?:

# Pattern: ca?t
# Matches:
'ct'
'cat'
# Does not match:
'caat'