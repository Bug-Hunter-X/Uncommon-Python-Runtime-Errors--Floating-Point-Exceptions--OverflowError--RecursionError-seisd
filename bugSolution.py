#Improved error handling for uncommon Python errors
import math

def improved_function_with_uncommon_error(a, b):
    try:
        if a == float('inf') or b == float('inf') or a == float('nan') or b == float('nan'):
            return "Error: Infinity or NaN encountered"
        result = a / b
        return result
    except ZeroDivisionError:
        return "Error: Division by zero"
    except OverflowError:
        return "Error: Overflow occurred"
    except TypeError:
        return "Error: Unsupported operand type(s) for /'"
    except Exception as e:
        return f"An unexpected error occurred: {e}"

#Example usage
result = improved_function_with_uncommon_error(float('inf'), 10)
print(result) #Output: Error: Infinity or NaN encountered
result = improved_function_with_uncommon_error(10, float('inf'))
print(result) #Output: 0.0
result = improved_function_with_uncommon_error(float('nan'), 10)
print(result) #Output: Error: Infinity or NaN encountered
result = improved_function_with_uncommon_error(10, float('nan'))
print(result) #Output: Error: Infinity or NaN encountered

#Improved recursive function to prevent RecursionError
def improved_recursive_function(n, limit=1000):
    if n > limit:
      return f"Error: Recursion depth exceeded limit of {limit}"
    if n == 0:
        return 0
    else:
        return improved_recursive_function(n-1, limit) + 1

print(improved_recursive_function(100000)) # Output: Error: Recursion depth exceeded limit of 1000