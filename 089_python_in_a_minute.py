# -*- coding: utf-8 -*-
"""089-Python in a minute.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10wSLjdQU7UZ723WpbTKSenNlBf7IGe45
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

# Backslash :

# Pattern: \.
# Matches:
# '.' (a period)
# Does not match:
# any character other than a period.

# Digits \d:

# Pattern: \d
# Matches:
# '0', '1', '2', ..., '9' (any single digit)
# Does not match:
# 'a', 'Z', ' ' (non-digit characters).

# Non-digits \D:

# Pattern: \D
# Matches:
# 'a', 'Z', ' ' (any non-digit character)
# Does not match:
# '0', '1', '2', ..., '9' (digits).

# Word characters \w:

# Pattern: \w
# Matches:
# 'a', 'Z', '3', '_' (any word character)
# Does not match:
# ' ', '@', '#' (non-word characters).

# Non-word characters \W:

# Pattern: \W
# Matches:
# ' ', '@', '#' (any non-word character)
# Does not match:
# 'a', 'Z', '3', '_' (word characters).
# Whitespace \s:

# Pattern: \s
# Matches:
# ' ', '\t', '\n' (any whitespace character)
# Does not match:
# 'a', 'Z', '3' (non-whitespace characters).

# Non-whitespace \S:

# Pattern: \S
# Matches:
# 'a', 'Z', '3' (any non-whitespace character)
# Does not match:
# ' ', '\t', '\n' (whitespace characters).