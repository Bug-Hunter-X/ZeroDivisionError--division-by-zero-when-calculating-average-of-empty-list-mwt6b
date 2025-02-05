def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list gracefully
    total = sum(numbers)
    average = total / len(numbers)
    return average

# Example usage with empty list:
my_numbers = []
average = calculate_average(my_numbers)
print(f"The average is: {average}")

# Example usage with numbers:
my_numbers = [10, 20, 30]
average = calculate_average(my_numbers)
print(f"The average is: {average}") 