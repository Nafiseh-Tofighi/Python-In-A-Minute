# -*- coding: utf-8 -*-
"""093-Python in a minute.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1DItPljyPnM8QdfFalfPdekLNg82ltLEP
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

import re

text = "Today is 26-06-2024. Yesterday was 25-06-2024."
pattern = r'\b\d{2}-\d{2}-\d{4}\b'

dates = re.findall(pattern, text)
print("Extracted dates:", dates)

email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

valid_email = "test.email@example.com"
invalid_email = "test.email@example"

print("Valid email check:", bool(re.match(email_pattern, valid_email)))
print("Invalid email check:", bool(re.match(email_pattern, invalid_email)))

text_with_repeats = "This is is a test test string"
repeated_word_pattern = r'\b(\w+)\s+\1\b'

repeated_words = re.findall(repeated_word_pattern, text_with_repeats)
print("Repeated words:", repeated_words)
