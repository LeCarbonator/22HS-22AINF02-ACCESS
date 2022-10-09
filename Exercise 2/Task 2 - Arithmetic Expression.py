
a = 1
b = 2
c = 3
d = 4

# Change the function below to calculate the result
# with the given formula:
# `a - (b^2 / (c - d * (a + b)))`
# You must use the variables defined above.


def calculate():
    # work from inside to outside
    res = (a + b) * d
    res = c - res
    res = b**2 / res
    res = a - res
    # You don't need to change the following line.
    # It simply returns the value calculated above.
    return res


# The following line calls the function and prints its return value. You don't
# need to change it, it's only here so you can see the result in the "Console
# Output" tab below
print(calculate())
