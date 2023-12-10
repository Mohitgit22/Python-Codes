# Example usage in another script

import my_moduleq4 as my_module

# Example data
my_numbers = (1, 5, 3, 7, 2)

# Using functions from my_module
total_sum = my_module.find_sum(my_numbers)
maximum_value = my_module.find_maximum(my_numbers)
minimum_value = my_module.find_minimum(my_numbers)

# Displaying results
print(f"Sum: {total_sum}")
print(f"Maximum: {maximum_value}")
print(f"Minimum: {minimum_value}")