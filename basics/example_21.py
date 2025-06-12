"""
JavaScript Array Method Equivalents in Python
"""

# JavaScript: array.map(x => x * 2)
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))  # [2, 4, 6, 8, 10]
doubled_comprehension = [x * 2 for x in numbers]  # More Pythonic way

# JavaScript: array.forEach(x => console.log(x))
for num in numbers:
    print(num)  # Prints each number

# JavaScript: array.reduce((acc, curr) => acc + curr, 0)
sum_numbers = sum(numbers)  # 15
# Or using reduce:
from functools import reduce
sum_reduce = reduce(lambda acc, curr: acc + curr, numbers, 0)  # 15

# JavaScript: array.find(x => x > 3)
first_greater_than_3 = next((x for x in numbers if x > 3), None)  # 4

# JavaScript: array.filter(x => x > 3)
greater_than_3 = list(filter(lambda x: x > 3, numbers))  # [4, 5]
greater_than_3_comprehension = [x for x in numbers if x > 3]  # More Pythonic way

# JavaScript: array.some(x => x > 3)
has_greater_than_3 = any(x > 3 for x in numbers)  # True

# JavaScript: array.every(x => x > 0)
all_positive = all(x > 0 for x in numbers)  # True 