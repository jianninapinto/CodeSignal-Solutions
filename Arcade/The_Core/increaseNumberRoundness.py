def solution(n):
    # Convert integer to a string
    n_str = str(n)
    # Get the index of the last character in the string number
    last_non_zero = len(n_str) - 1
    # Iterate through the string to find the rightmost non-zero digit
    while last_non_zero >= 0 and n_str[last_non_zero] == '0':
        last_non_zero -= 1 # decrement by 1 until a non-0 digit is found
        print(last_non_zero)
    # Non-zero digits before the trailing zeros
    if last_non_zero == -1:
        return False
    
    for i in range(last_non_zero):
        if n_str[i] == '0':
            n_str = n_str[:i] + n_str[last_non_zero] + n_str[i+1:last_non_zero] + '0' + n_str[last_non_zero+1:]
            return True
    
    return False

"""
Define an integer's roundness as the number of trailing zeroes in it.

Given an integer n, check if it's possible to increase n's roundness by swapping some pair of its digits.

Example

For n = 902200100, the output should be
solution(n) = true.

One of the possible ways to increase roundness of n is to swap digit 1 with digit 0 preceding it: roundness of 902201000 is 3, and roundness of n is 2.

For instance, one may swap the leftmost 0 with 1.

For n = 11000, the output should be
solution(n) = false.

Roundness of n is 3, and there is no way to increase it.

Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] integer n

A positive integer.

Guaranteed constraints:
100 ≤ n ≤ 109.

[output] boolean

true if it's possible to increase n's roundness, false otherwise.
"""