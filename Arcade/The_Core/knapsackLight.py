def solution(value1, weight1, value2, weight2, maxW):
    # Calculate total weight for both items
    total_weight = weight1 + weight2
    # Check if total weight is less or equal to max weight capacity
    if total_weight <= maxW:
        total_max_value = value1 + value2
        return total_max_value # sum of both items values
    else:
        # If each item w is greater than max W
        if weight1 > maxW and weight2 > maxW:
            return 0 # can't bring any of the items - too heavy
        # If items lighter than max w capacity
        elif weight1 <= maxW and weight2 <= maxW:
            return max(value1, value2) # bring item with highest value
        else:
            # If item 1 lighter than max w capacity
            if weight1 <= maxW:
                return value1 # bring that item
            else:
                return value2 # bring item 2
            

"""
You found two items in a treasure chest! The first item weighs weight1 and is worth value1, and the second item weighs weight2 and is worth value2. What is the total maximum value of the items you can take with you, assuming that your max weight capacity is maxW and you can't come back for the items later?

Note that there are only two items and you can't bring more than one item of each type, i.e. you can't take two first items or two second items.

Example

For value1 = 10, weight1 = 5, value2 = 6, weight2 = 4, and maxW = 8, the output should be
solution(value1, weight1, value2, weight2, maxW) = 10.

You can only carry the first item.

For value1 = 10, weight1 = 5, value2 = 6, weight2 = 4, and maxW = 9, the output should be
solution(value1, weight1, value2, weight2, maxW) = 16.

You're strong enough to take both of the items with you.

For value1 = 5, weight1 = 3, value2 = 7, weight2 = 4, and maxW = 6, the output should be
solution(value1, weight1, value2, weight2, maxW) = 7.

You can't take both items, but you can take any of them.

Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] integer value1

Guaranteed constraints:
2 ≤ value1 ≤ 20.

[input] integer weight1

Guaranteed constraints:
2 ≤ weight1 ≤ 10.

[input] integer value2

Guaranteed constraints:
2 ≤ value2 ≤ 20.

[input] integer weight2

Guaranteed constraints:
2 ≤ weight2 ≤ 10.

[input] integer maxW

Guaranteed constraints:
1 ≤ maxW ≤ 20.

[output] integer
"""