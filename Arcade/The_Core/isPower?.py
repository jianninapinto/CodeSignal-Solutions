def solution(n):
    # base case
    if n == 1:
        return True
    # iterate over all integers from 0 to the sqr of n inclusive
    for i in range(2, int(n ** 0.5) + 1):
        # iterate over all integers from 0 to 9 inclusive
        for j in range(10):
            # for each combination of i and j 
            # check if i raised to the power of j equals n
            if i ** j == n:
                return True
    return False


# Determine if the given number is a power of some non-negative integer.

# Example

# For n = 125, the output should be
# solution(n) = true;
# For n = 72, the output should be
# solution(n) = false.
# Input/Output

# [execution time limit] 4 seconds (py3)

# [memory limit] 1 GB

# [input] integer n

# A positive integer.

# Guaranteed constraints:
# 1 ≤ n ≤ 400.

# [output] boolean

# true if n can be represented in the form ab (a to the power of b) where a and b are some non-negative integers and b ≥ 2, false otherwise.