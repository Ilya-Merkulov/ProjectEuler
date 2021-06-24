"""
By considering the terms in the Fibonacci sequence whose values do not exceed four million,
find the sum of the even-valued terms.
"""
"""
# Python program to print prime factors

import math

# A function to print all prime factors of
# a given number n
from typing import Dict, Any


def prime_factors(n):
    result = set()
    # Print the number of two's that divide n
    while n % 2 == 0:
        result.add(2)
        n = n / 2

    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3, int(math.sqrt(n)) + 1, 2):

        # while i divides n , print i ad divide n
        while n % i == 0:
            result.add(i)
            n = n / i

    # Condition if n is a prime
    # number greater than 2
    if n > 2:
        result.add(n)

    print(result)


# Driver Program to test above function

m = 16#13195
prime_factors(m)
"""


# my result - "?"


def prime_factors(num):
    result = []
    i = 3

    while i <= num:
        if num % i == 0:
            num /= i
            result.append(i)
        else:
            i += 2

    print(result)


prime_factors(12)



p = 24
print(max(x for x in range(2, p) if p % x == 0))