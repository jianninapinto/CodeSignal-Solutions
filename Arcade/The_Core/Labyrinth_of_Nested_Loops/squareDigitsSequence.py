def solution(a0):
    sequence = [a0] # Initialize an empty list to store the sequence of elements starting with a0
    current_sum = 0 # Initialize a variable to track the sum of the digits of the current element
    
    # Calculate the sum of squared digits for the initial element a0
    while a0:
        current_sum += pow((a0 % 10), 2) # Add the square of the last digit to the sum for the current element
        a0 //= 10 # Update the value of a0 by removing the last digit until a0 becomes 0
        
    # Continue looping until a repeating element is found in the sequence
    while current_sum not in sequence:
        sequence.append(current_sum) # Add the current element to the sequence list
        a0 = current_sum # Update a0 with the current element to prepare for the next iteration
        current_sum = 0 # Reset the current sum 
        
        # Calculate the sum of squared digits of new element
        while a0:
            current_sum += pow((a0 % 10), 2)
            a0 //= 10
    return len(sequence) + 1 # Return the length of the sequence (+1 for the repeated element)

"""
Consider a sequence of numbers a0, a1, ..., an, in which an element is equal to the sum of squared digits of the previous element. The sequence ends once an element that has already been in the sequence appears again.

Given the first element a0, find the length of the sequence.

Example

For a0 = 16, the output should be
solution(a0) = 9.

Here's how elements of the sequence are constructed:

a0 = 16
a1 = 12 + 62 = 37
a2 = 32 + 72 = 58
a3 = 52 + 82 = 89
a4 = 82 + 92 = 145
a5 = 12 + 42 + 52 = 42
a6 = 42 + 22 = 20
a7 = 22 + 02 = 4
a8 = 42 = 16, which has already occurred before (a0)
Thus, there are 9 elements in the sequence.

For a0 = 103, the output should be
solution(a0) = 4.

The sequence goes as follows: 103 -> 10 -> 1 -> 1, 4 elements altogether.

Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] integer a0

First element of a sequence, positive integer.

Guaranteed constraints:
1 ≤ a0 ≤ 105.

[output] integer
"""