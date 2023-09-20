# Chained conditions combine multiple conditions to form one.print

# Conditions

# and : both have to be true else the statement is false
# or : one of them has to be true or false, if both are false, it is false.
# not : is True if one value is false

x = 7
y = 15
z = 5

result1 = x ==y
result2 = y > x
result3 = z < x +2

result4 = result1 or result2 or result3 # This creates a condition that one one the statements has to be true else both have to be false.
print(result4)

result5 = result1 and result2
print(result5)