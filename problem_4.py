"""
Find the largest palindrome made from the product of two 3-digit numbers.
"""
# my shit result
def the_largest_palindrome():
    # calculations
    i = 999
    j = 998
    while i != 100:
        # is_it_palindrome
        step_j = j
        while step_j != 100:
            if is_it_palindrome(i*j):
                print(i,j)
                return (i*j)
            step_j -= 1
        j -= 1
        i -= 1


    print("is no palindrome")
    return 0
    # result

def is_it_palindrome(n):
    #calculations
    flag = False

    str_n = str(n)
    str_n_revers = str_n[::-1]
    if str_n == str_n_revers:
        flag = True

    # result(true/false)
    return flag


#print(the_largest_palindrome())


# genius
print(max([x*y for x in range(900,1000) for y in range(900,1000) if str(x*y) == str(x*y)[::-1]]))






