"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""

# my first result
def multiples(a, b):
    sum = 0
    for i in range(1, 1000):
        if i % a == 0 or i % b == 0:
            sum += i
    return sum


print(multiples(3, 5))


# more general result
def divisible_by_under(limit, divs):
    return (i for i in range(limit) if any(i % div == 0 for div in divs))


print(sum(divisible_by_under(1000, (3, 5))))


# list comprehension

print(sum([i for i in range(1, 1000) if i % 3 == 0 or i % 5 == 0]))
