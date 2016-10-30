"""
String Formatting
"""

# Standard C-printf way
print("There are %d days in a year" % 365)


# Alternative
s = "My name is {} {}"
print(s.format('David', 'Becerra'))


# Using keyword arguments
s = "{subject} is {opinion}"
print(s.format(opinion="fun", subject="Math"))