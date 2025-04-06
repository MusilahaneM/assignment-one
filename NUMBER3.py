calculate_average(*args):
"""
Calculate the average of a variable number of numerical arguments.

Parameters:
    *args (float or int): A variable number of numerical values.

Returns:
    float: The average of the input numbers. Returns None if no numbers are provided.
"""
try:
    if not args:
        return None

    return sum(args) / len(args)
except ValueError:
    print("Error: Invalid number input. Please enter valid numerical values.")
    return None
