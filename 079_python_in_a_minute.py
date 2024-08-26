# -*- coding: utf-8 -*-
"""079-Python in a minute.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1GnXkMkztYuif7os8FsTwGoFQCj2YhO1v
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

#re.findall(pattern, string, flags=0)

import re

text = "hello world hello"
result = re.findall(r'hello', text)
print(result)  # Output: ['hello', 'hello']

text = "abc 123 def 456"
result = re.findall(r'\d+', text)
print(result)  # Output: ['123', '456']

text = "Python is great. I love python."
result = re.findall(r'python', text, re.IGNORECASE)
print(result)  # Output: ['Python', 'python']
