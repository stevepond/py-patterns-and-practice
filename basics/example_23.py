"""
While Loops in Python
"""

# Basic while loop
count = 0
while count < 5:
    print(count)
    count += 1

# While loop with break
number = 0
while True:
    if number == 5:
        break
    print(number)
    number += 1

# While loop with continue
num = 0
while num < 10:
    num += 1
    if num % 2 == 0:
        continue
    print(num)  # Prints only odd numbers

# While loop with else clause
# The else clause executes when the while condition becomes false
counter = 0
while counter < 3:
    print(counter)
    counter += 1
else:
    print("Loop completed!")

# While loop for input validation
# This is a common pattern for getting valid user input
def validate_age(input_age):
    """Validate age input and return True if valid, False otherwise."""
    try:
        age = int(input_age)
        return 0 <= age <= 120
    except ValueError:
        return False

# While loop for processing a list
numbers = [1, 2, 3, 4, 5]
index = 0
while index < len(numbers):
    print(numbers[index] * 2)
    index += 1 