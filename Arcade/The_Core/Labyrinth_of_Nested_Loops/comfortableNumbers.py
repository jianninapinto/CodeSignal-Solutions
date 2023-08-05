def solution(l, r):
    count = 0 # Initialize a count for the number of pairs
    
    # Iterate through the numbers from l to r (exclusive)
    for a in range(l, r):
        s_a = sum([int(s) for s in str(a)]) # Calculate sum of digits for number a
        
        # Iterate through numbers from a + 1 to r inclusive
        for b in range(a+1, r+1):
            s_b = sum([int(s) for s in str(b)]) # Calculate the sum of digits for number b
            
            # Check if both numbers feel comfortable with each other
            if a - s_a <= b <= a + s_a and b - s_b <= a <= b + s_b:
                count += 1 # Increment the count for valid pairs
                
    return count # Return the total number of valid pairs

"""
Let's say that number a feels comfortable with number b if a ≠ b and b lies in the segment [a - s(a), a + s(a)], where s(x) is the sum of x's digits.

How many pairs (a, b) are there, such that a < b, both a and b lie on the segment [l, r], and each number feels comfortable with the other (so a feels comfortable with b and b feels comfortable with a)?

Example

For l = 10 and r = 12, the output should be
solution(l, r) = 2.

Here are all values of s(x) to consider:

s(10) = 1, so 10 is comfortable with 9 and 11;
s(11) = 2, so 11 is comfortable with 9, 10, 12 and 13;
s(12) = 3, so 12 is comfortable with 9, 10, 11, 13, 14 and 15.
Thus, there are 2 pairs of numbers comfortable with each other within the segment [10; 12]: (10, 11) and (11, 12).

Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] integer l

Guaranteed constraints:
1 ≤ l ≤ r ≤ 1000.

[input] integer r

Guaranteed constraints:
1 ≤ l ≤ r ≤ 1000.

[output] integer

The number of pairs satisfying all the above conditions.
"""