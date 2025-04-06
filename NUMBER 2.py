def calculate_average(*args):
    """
    Calculate the average of a variable number of arguments.

    Parameters:
    *args: A variable number of numerical arguments.

    Returns:
    float: The average of the provided numbers. Returns None if no numbers are provided.
    """
    if not args:
        return None  # Return None if no arguments are provided

    total = sum(args)  # Calculate the sum of the arguments
    count = len(args)  # Get the number of arguments
    average = total / count  # Calculate the average
    return average

# Example of calling the function
result = calculate_average(10, 20, 30, 40, 50)
print(result)  # Output: 30.0