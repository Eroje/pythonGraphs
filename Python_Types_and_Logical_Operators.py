# Python Type

# Basic types in python!
print(type("Hello World"))
print(type(13))
print(type(4.72))
print(type(True))

# Moving to Integers
print(4.72, int(4.72))  # Python rounds down!
print (4.05, int(4.05))

# Rounding Up!
print(4.72, int(4.72), int(round(4.72)))

# Logical operators
# There are three different logical operators; 'and', 'or', 'not'

x = 6
print(x > 0 and x < 10)  # and means both must hold
print(0 < x < 10)

y = 9
print(y % 2 == 0 or y % 3 == 0)  # or means one must hold

