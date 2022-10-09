price_cone = 0.70
price_per_scoop_vanilla = 1.00
price_per_scoop_chocolate = 1.10

num_scoops_vanilla = 1
num_scoops_chocolate = 3

# Change the function below to calculate the total price this
# order. Note that your implementation should work with any
# specific value, so you can't just add up the raw numbers,
# you MUST use the VARIABLES defined above. Do not forget the
# cone!


def get_price():
    #   cone
    # + num_vanilla * price_vanilla
    # + num_chocolate * price_chocolate
    # ────────────────────────────
    #   price
    price_vanilla = num_scoops_vanilla * price_per_scoop_vanilla
    price_chocolate = num_scoops_chocolate * price_per_scoop_chocolate
    price = price_cone + price_vanilla + price_chocolate
    # You don't need to change the following line
    return price


# The following line calls the function and prints its return value. You don't
# need to change it, it's only here so you can see the result in the "Console
# Output" tab below
print(get_price())
