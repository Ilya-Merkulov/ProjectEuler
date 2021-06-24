"""
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

def divisible():
    rez = 2
    for i in range(3, 20):
        if rez % i == 0:
            continue
        else:
            rez = rez * i
            print(rez)


    return rez


print(divisible())