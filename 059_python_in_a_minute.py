# -*- coding: utf-8 -*-
"""059-Python in a minute.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-Hy9PzB-DSz_WnZbo9zUksnfwxSzl1Pf
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

# Translation table with two strings
trans_table = str.maketrans('he', 'ya')
text = "hello"
result = text.translate(trans_table)
print(result)  # Output: yallo

# Translation table with a dictionary
trans_table = str.maketrans({'h': 'y', 'e': 'a'})
text = "hello"
result = text.translate(trans_table)
print(result)  # Output: yallo

# Translation table to remove characters
trans_table = str.maketrans('', '', 'aeiou')
text = "hello"
result = text.translate(trans_table)
print(result)  # Output: hll