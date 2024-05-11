"""
File: 019-MembershipOperators-Python_In_A_Minute.py
Author: Nafiseh J.Tofighi
Date: 11May2024

Description:
This script provides an overview of membership operators in Python along with their explanations and examples.

Usage:
- Review the table to understand each membership operator's symbol and explanation.
- Run the script to see examples of membership operations using these operators.
"""


"""

| Operator | Example            | Explanation                                                         |
|----------|--------------------|---------------------------------------------------------------------|
| in       | x in sequence      | Returns True if x is found in the specified sequence.               |
| not in   | x not in sequence  | Returns True if x is not found in the specified sequence.           |
"""

# Example with Strings
string = "hello"
substring1 = "he"
substring2 = "world"

# in Operator
result_in_substring1 = substring1 in string
result_in_substring2 = substring2 in string
print("Substring 'he' in 'hello':", result_in_substring1)  # Output: True
print("Substring 'world' in 'hello':", result_in_substring2)  # Output: False

# not in Operator
result_not_in_substring1 = substring1 not in string
result_not_in_substring2 = substring2 not in string
print("Substring 'he' not in 'hello':", result_not_in_substring1)  # Output: False
print("Substring 'world' not in 'hello':", result_not_in_substring2)  # Output: True

# Example with Lists
my_list = [1, 2, 3, 4, 5]
element1 = 3
element2 = 6

# in Operator
result_in_element1 = element1 in my_list
result_in_element2 = element2 in my_list
print("Element 3 in list:", result_in_element1)  # Output: True
print("Element 6 in list:", result_in_element2)  # Output: False

# not in Operator
result_not_in_element1 = element1 not in my_list
result_not_in_element2 = element2 not in my_list
print("Element 3 not in list:", result_not_in_element1)  # Output: False
print("Element 6 not in list:", result_not_in_element2)  # Output: True

