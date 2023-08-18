def solution(n):
    # Initialize counter to keep track of the number of valid representations
    c = 0 
    # Iterate through possible starting values from 1 to (n-1) 
    for i in range(1, n): 
        # Initialize the current sum to the starting value i 
        s = i  
        # Iterate through consecutive positive int from i+1
        for j in range(i + 1, n):  
            # Add the current positive integer j to the current sum
            s += j  
            # If the current sum equals n, a valid representation is found
            if s == n:  
                # Increment the counter as we found one valid representation
                c += 1  
            # If the current sum becomes greater than n, break the loop
            elif s > n:
                break
    # Return the total count of valid representations
    return c  

"""
Find the number of ways to express n as sum of some (at least two) consecutive positive integers.

Example

For n = 9, the output should be
solution(n) = 2.

There are two ways to represent n = 9: 2 + 3 + 4 = 9 and 4 + 5 = 9.

For n = 8, the output should be
solution(n) = 0.

There are no ways to represent n = 8.

Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] integer n

A positive integer.

Guaranteed constraints:
1 ≤ n ≤ 104.

[output] integer

"""
