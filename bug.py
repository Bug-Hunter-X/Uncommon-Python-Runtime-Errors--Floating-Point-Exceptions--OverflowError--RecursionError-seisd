def function_with_uncommon_error(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Error: Division by zero"
    except TypeError:
        return "Error: Unsupported operand type(s) for /'"

# Uncommon error scenario: Floating-point exception
result = function_with_uncommon_error(float('inf'), 10)
print(result)  # Output: inf
result = function_with_uncommon_error(10, float('inf'))
print(result)  # Output: 0.0
result = function_with_uncommon_error(float('nan'), 10)
print(result) # Output: nan
result = function_with_uncommon_error(10, float('nan'))
print(result) # Output: nan

#Another uncommon error scenario
import math

# Example of OverflowError
# This error occurs when the result of a calculation is too large to be represented.
# It is less common than ZeroDivisionError or TypeError, but can still occur in numerical computations.
result = math.exp(1000)
print(result) #Output: inf

# Example of RecursionError
#This error occurs when a recursive function calls itself too many times.
#It is less common than other runtime errors but can happen in poorly designed recursive functions. 
def recursive_function(n):
    if n == 0:
        return 0
    else:
        return recursive_function(n-1) + 1

#This is not an error
recursive_function(1000)
#This will cause a recursion error
recursive_function(100000)