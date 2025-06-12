"""
If/Else Statements and Ternary Operations in Python
"""

# Basic if/else
age = 20
if age >= 18:
    status = "adult"
else:
    status = "minor"

# if/elif/else
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

# Ternary operator (conditional expression)
# JavaScript: const status = age >= 18 ? "adult" : "minor"
status = "adult" if age >= 18 else "minor"

# Nested ternary (though not recommended for readability)
# JavaScript: const message = age >= 18 ? (score >= 90 ? "Adult A" : "Adult B") : "Minor"
message = "Adult A" if age >= 18 and score >= 90 else "Adult B" if age >= 18 else "Minor"

# Multiple conditions
is_weekend = True
is_holiday = False
if is_weekend and not is_holiday:
    activity = "relax"
elif is_holiday:
    activity = "celebrate"
else:
    activity = "work"

# Using 'in' operator for multiple conditions
month = "July"
if month in ["June", "July", "August"]:
    season = "summer"
elif month in ["December", "January", "February"]:
    season = "winter"
else:
    season = "other" 