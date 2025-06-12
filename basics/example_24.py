"""
Dictionary Iteration in Python (similar to Object.entries() in JavaScript)
"""

# Sample dictionary
person = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "occupation": "Developer"
}

# JavaScript: Object.entries(person).forEach(([key, value]) => console.log(key, value))
# Method 1: Using .items()
for key, value in person.items():
    print(f"{key}: {value}")

# Method 2: Using .keys() and .values() separately
for key in person.keys():
    print(f"Key: {key}")

for value in person.values():
    print(f"Value: {value}")

# Method 3: Using enumerate() with items()
for index, (key, value) in enumerate(person.items()):
    print(f"Index {index}: {key} = {value}")

# Method 4: Dictionary comprehension (similar to JavaScript's map)
# JavaScript: Object.entries(person).map(([key, value]) => [key, value.toUpperCase()])
uppercase_values = {k: v.upper() if isinstance(v, str) else v for k, v in person.items()}

# Method 5: Filtering dictionary items
# JavaScript: Object.entries(person).filter(([key, value]) => typeof value === 'string')
string_values = {k: v for k, v in person.items() if isinstance(v, str)}

# Method 6: Creating a list of tuples (similar to Object.entries())
entries = list(person.items())  # [('name', 'John'), ('age', 30), ...]

# Method 7: Iterating with custom formatting
for key, value in person.items():
    if isinstance(value, str):
        print(f"The {key} is '{value}'")
    else:
        print(f"The {key} is {value}") 