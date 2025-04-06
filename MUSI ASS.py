def calculate_average(*args):
    """
    Calculate the average of a variable number of numerical arguments.

    Parameters:
        *args (float or int): A variable number of numerical values.

    Returns:
        float: The average of the input numbers. Returns None if no numbers are provided.
    """
    if not args:
        return None

    return sum(args) / len(args)


# Example usage
print(calculate_average(10, 20, 30))  # Output: 20.0

