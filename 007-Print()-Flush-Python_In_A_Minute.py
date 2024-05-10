"""
File: 007-Print()-Flush-Python_In_A_Minute.py
Author: Nafiseh J.Tofighi
Date: 10May2024

Description:
This script demonstrates the usage of the 'flush' parameter in the print() function to control the flushing behavior of the output buffer.

Usage:
- Run the script to see examples of printing with and without flush.
"""

import time

print('Start with flush')
for i in range(10):
  print('*', end=' ', flush=True)
  time.sleep(0.5)
print('\nDone')

#output: Start with flush
# * * * * * * * * * * 
# Done


print('Start without flush')
for i in range(10):
  print('*', end=' ', flush=False)
  time.sleep(0.5)
print('\nDone')

#output: Start without flush
# * * * * * * * * * * 
# Done
