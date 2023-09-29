def solution(arr):
    # Check if array has an odd length    
    if len(arr) %2 !=0:
        # Calculate middle index
        middle_index = len(arr)//2
        # Assign the middle value to element at that index
        middle_value= arr[middle_index]
        
    else: # if array has an even length
        # Calculate the two middle indexes
        middle_index1 = int(len(arr) / 2) - 1
        middle_index2 = int(len(arr) / 2)
        # Assign the mid value to both elements at those indexes
        middle_value = arr[middle_index1] + arr[middle_index2]
    
    # If first element, middle element, and last element are equal
    # return true, else false
    return middle_value == arr[0] and middle_value == arr[-1]

"""
We define the middle of the array arr as follows:

if arr contains an odd number of elements, its middle is the element whose index number is the same when counting from the beginning of the array and from its end;
if arr contains an even number of elements, its middle is the sum of the two elements whose index numbers when counting from the beginning and from the end of the array differ by one.
An array is called smooth if its first and its last elements are equal to one another and to the middle. Given an array arr, determine if it is smooth or not.

Example

For arr = [7, 2, 2, 5, 10, 7], the output should be
solution(arr) = true.

The first and the last elements of arr are equal to 7, and its middle also equals 2 + 5 = 7. Thus, the array is smooth and the output is true.

For arr = [-5, -5, 10], the output should be
solution(arr) = false.

The first and middle elements are equal to -5, but the last element equals 10. Thus, arr is not smooth and the output is false.

Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.integer arr

The given array.

Guaranteed constraints:
2 ≤ arr.length ≤ 105,
-109 ≤ arr[i] ≤ 109.

[output] boolean

true if arr is smooth, false otherwise.
"""