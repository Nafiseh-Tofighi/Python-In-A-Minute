"""
File: 012-NamingConventions-Python_In_A_Minute.py
Author: Nafiseh J.Tofighi
Date: 10May2024

Description:
This script illustrates the rules and conventions for naming variables in Python.

Rules:
- Variables can consist of uppercase and lowercase a-z characters.
- They can contain underscores.
- They can include digits, but not at the beginning.
- They support Unicode characters.

Conventions:
- Variables should have meaningful names.
- They can be of any length.
- Variable names are case-sensitive.
- They cannot use reserved keywords.

Usage:
- Run the script to see examples of valid and invalid variable names.
"""

"""
* Uppercase and lowercase a-z characters

* Underscore

* Digits(not at the beginning)

* Unicode
"""

Hello= 'World'

print(Hello)

temp_var= 5
_temp_var= 10

print(_temp_var, temp_var)

var2= 10
# 2var= 10

vär= 10

print(vär)

"""
* Any length
* Case sensitive
* Cannot use reserved keywords
"""

a= 'Hello,'
A= 'World!'

print(a, A)