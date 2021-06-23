"""
By considering the terms in the Fibonacci sequence whose values do not exceed four million,
find the sum of the even-valued terms.
"""


# my result

# fibonacci -> less(<) 4m-> is this even-valued -> sum

def fibonacci_even_valued():
    max_value = 4000000
    total_sum = 2
    a = 1
    b = 2
    while (b < max_value):
        b, a = b + a, b
        if b % 2 == 0:
            total_sum += b

    return total_sum


print(fibonacci_even_valued())


