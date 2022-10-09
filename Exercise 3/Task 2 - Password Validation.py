
# -  Has a length of 8-16 chars.

# -  Only contains the characters a-z, A-Z, digits,
#      or the special chars "+", "-", "*", "/".

# -  Must contain at least 2 lower case and 2 upper case characters,
#      2 digits, and 2 special chars.


pwd = "aaaaAAAA0000++++"


def is_valid():
    # You need to change the following part of the function
    # to determine if it is a valid password.
    validity = False
    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0
    hasInvalidChars = False
    for char in pwd:
        if char.islower():
            # 'x += 1' is the same as 'x = x + 1'
            count_lower += 1
            continue
        if char.isupper():
            count_upper += 1
            continue
        if char.isdigit():
            count_digit += 1
            continue
        # 'in' checks if char exists within an iterable.
        if char in "+-*/":
            count_special += 1
            continue
        # the only way none of the
        # statements were fired is if
        # the character is not allowed
        hasInvalidChars = True

    # verify that all character requirements were met (2 or more of each)
    if count_lower >= 2 and count_upper >= 2 and count_digit >= 2 and count_special >= 2:
        validity = True
    # check for invalid characters and pw length
    if hasInvalidChars or len(pwd) < 8 or len(pwd) > 16:
        validity = False

    # You don't need to change the following line.
    return validity


# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
print(is_valid())
