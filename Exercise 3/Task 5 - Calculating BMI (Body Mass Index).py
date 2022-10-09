#!/usr/bin/env python3

# Height in M
height = -1
# Weight in KG
weight = 10


# Determine the BMI. Change the function
# below to calculate the BMI return which category the result is in.
# Your implementation should work with any specific value.
# You must use the variables defined above.


def get_bmi_category():
    # We do not accept weight or height below zero.
    # Confused by this if statement's structure?
    # Look up 'Guard Clauses'
    if weight < 0 or height < 0:
        return "N/A"

    bmi = weight / height ** 2
    ctg = ""

    # elif is vital here.
    # otherwise
    #    elif bmi > 35
    # would turn into
    #    if bmi <=40 and bmi > 35
    if bmi > 40:
        ctg = "Obesity class III"
    elif bmi > 35:
        ctg = "Obesity class II"
    elif bmi > 30:
        ctg = "Obesity class I"
    elif bmi > 25:
        ctg = "Pre-obesity"
    elif bmi > 18.5:
        ctg = "Normal weight"
    elif bmi >= 0:
        ctg = "Underweight"

    # :.2f rounds to 2 points after the decimal.
    # Note the dot before the 2f.
    return f"BMI: {bmi:.2f}, Category: {ctg}"


# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
print(get_bmi_category())
