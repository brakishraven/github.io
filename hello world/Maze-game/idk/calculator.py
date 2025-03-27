import scipy.integrate as integrate
import numpy as np
import matplotlib as plt
from sympy.utilities.lambdify import lambdify
def calculate_integral(function_str, lower_limit, upper_limit):
    """
    Calculates the definite integral of a function.

    Args:
        function_str: The function to integrate, as a string (e.g., "x**2 + 1").
        lower_limit: The lower limit of integration.
        upper_limit: The upper limit of integration.

    Returns:
        The result of the definite integral, or an error message if input is invalid.
    """
    try:
        # Convert the function string to a callable function
        function = lambda x: eval(function_str)

        # Calculate the integral
        result, error = integrate.quad(function, lower_limit, upper_limit)
        return result
    except (SyntaxError, NameError, TypeError) as e:
        return f"Error: Invalid input: {e}"
    except Exception as e:
         return f"An unexpected error occurred: {e}"

if __name__ == "__main__":
    function_input = input("Enter the function to integrate (e.g., x**2 + 1): ")
    try:
        lower_limit_input = float(input("Enter the lower limit of integration: "))
        upper_limit_input = float(input("Enter the upper limit of integration: "))
    except ValueError:
        print("Error: Please enter numeric values for the limits.")
    else:
         integral_result = calculate_integral(function_input, lower_limit_input, upper_limit_input)
         print("Result of the definite integral:", integral_result)