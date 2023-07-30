def calculate_factorial(n):
    """
    Calculate the factorial of a given positive integer.

    Args:
        n (int): The positive integer for which the factorial will be calculated.

    Returns:
        int: The factorial value of the input integer.

    Raises:
        ValueError: If the input is not a positive integer.
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer.")
    
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i

    return factorial

print('3!= ', calculate_factorial(3))
# print(calculate_factorial.__doc__)