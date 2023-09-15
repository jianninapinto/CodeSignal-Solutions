def solution(param1, param2):
    # initialize the result to 0
    result = 0
    
    # initialize the multiplier to 1
    multiplier = 1
    
    # iterate until both numbers are 0
    while param1 > 0 or param2 > 0:
        # add the last digits of both numbers, ignoring any carry
        digit_sum = (param1 % 10 + param2 % 10) % 10
        
        # add the digit sum to the result, multiplied by the current multiplier
        result += digit_sum * multiplier
        
        # divide both numbers by 10 to remove the last digit
        param1 //= 10
        param2 //= 10
        
        # multiply the multiplier by 10 for the next iteration
        multiplier *= 10
    
    # return the result
    return result


"""
A little child is studying arithmetic. They have just learned how to add two integers, written one below another, column by column. But the child always forgets about the important part - carrying.

Given two integers, your task is to find the result that the child will get.

Note: The child had learned from this site, so feel free to check it out too if you are not familiar with column addition.

Example

For param1 = 456 and param2 = 1734, the output should be
solution(param1, param2) = 1180.

   456
  1734
+ ____
  1180
The child performs the following operations from right to left:

6 + 4 = 10 but the child forgets about carrying the 1 and just writes down the 0 in the last column
5 + 3 = 8
4 + 7 = 11 but the child forgets about the leading 1 and just writes down 1 under 4 and 7.
There is no digit in the first number corresponding to the leading digit of the second one, so the child imagines that 0 is written before 456. Thus, they get 0 + 1 = 1.
Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] integer param1

A non-negative integer.

Guaranteed constraints:
0 ≤ param1 < 105.

[input] integer param2

A non-negative integer.

Guaranteed constraints:
0 ≤ param2 < 6 · 104.

[output] integer

The result that the little child will get by using column addition without carrying.
"""