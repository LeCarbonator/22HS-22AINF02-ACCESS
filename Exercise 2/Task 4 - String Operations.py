s = "aB:cD"

# perform the transformation


def transform_string():
    # Insert your code here.
    # You may want to use several variables to
    # store temporary values (such as the index of
    # the colon or the two strings before and after
    # it). Then, you can construct the final result
    # from your temporary variables.

    # find the index of the colon
    colon_pos = s.find(":")
    # [:colon_pos] excludes the :, while [colon_pos:] includes it.
    # You do not need to add the : back.
    res = s[:colon_pos].lower() + s[colon_pos:].upper()

    # You don't need to change the following line.
    # It simply returns the string created above.
    return res


# The following line calls the function and prints its return value. You don't
# need to change it, it's only here so you can see the result in the "Console
# Output" tab below
print(transform_string())
print()  # extra newline at the end
