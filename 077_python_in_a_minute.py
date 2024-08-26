# -*- coding: utf-8 -*-
"""077-Python in a minute.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1AipqNhNPP0jkYqjpA-io-IloYocNtvgs
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

# re.match(pattern, string, flags=0)

import re

text = "hello world"
result = re.match(r'hello', text)
print(result)

text = "hello world"
result = re.match(r'world', text)
print(result)

text = "Hello world"
result = re.match(r'hello', text, re.IGNORECASE)
print(result)

