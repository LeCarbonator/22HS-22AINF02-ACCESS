#!/usr/bin/env python3

# As mentioned in the hints, you might want to use the math package
import math

# You can change this value to your liking. Depending on your implementation larger values of n might take quite some time.
n = 13

# perform the Sieve of Eratosthenes algorithm and return all primes <= n


def sieve_of_eratosthenes():
    primes_up_to_n = []
    marked_numbers = []
    curr_prime = 2

    # we only check up to the square root of n
    while curr_prime * curr_prime <= n:
        # not marked
        # the 'in' operator checks if an element is within an iterable
        # -> char in string, element in array
        if curr_prime not in marked_numbers:
            # if it's not marked, we add it to prime numbers, and remove all multiples
            primes_up_to_n.append(curr_prime)
            # starting point is squared because any less
            # would be multiples of previous numbers
            #     !!
            # 4 * 2 = 8 -> dividable by 2 already

            # our for loop starts at x^2, ends at n+1 (excluding it), and goes x
            # steps forward every loop.
            for num in range(curr_prime * curr_prime, n+1, curr_prime):
                marked_numbers.append(num)
        # don't forget! We cause an infinite loop otherwise
        curr_prime += 1

    # we reached the square root of n. Simply loop through the rest
    # and check if they've been marked.
    # make sure to INCLUDE n. EXAMPLE: n = 13
    for num in range(curr_prime, n + 1, 1):
        if num in marked_numbers:
            continue
        primes_up_to_n.append(num)

    # in case the array is empty
    if len(primes_up_to_n) == 0:
        primes_up_to_n.append("empty")

    return primes_up_to_n


# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
print(sieve_of_eratosthenes())
