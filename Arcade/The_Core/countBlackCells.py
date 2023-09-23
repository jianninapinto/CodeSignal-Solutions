def solution(n, m):
    # line formula
    # y-int = n
    # slope = -(n/m)
    # y = -(n/m) x + n
    def ycoord(x):
        return -(n/m) * x + n

    tot = 0
    
    for x in range(m):
        start = ycoord(x)
        if start % 1 == 0 and x > 0:
            tot += 1
        end = ycoord(x+1)
        if end % 1 == 0 and x < m-1:
            tot += 1
        start = math.ceil(start)
        end = math.floor(end)
        covered = math.ceil(start - end)
        
        tot += covered
    return tot

"""
Imagine a white rectangular grid of n rows and m columns divided into two parts by a diagonal line running from the upper left to the lower right corner. Now let's paint the grid in two colors according to the following rules:

A cell is painted black if it has at least one point in common with the diagonal;
Otherwise, a cell is painted white.
Count the number of cells painted black.

Example

For n = 3 and m = 4, the output should be
solution(n, m) = 6.

There are 6 cells that have at least one common point with the diagonal and therefore are painted black.



For n = 3 and m = 3, the output should be
solution(n, m) = 7.

7 cells have at least one common point with the diagonal and are painted black.



Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] integer n

The number of rows.

Guaranteed constraints:
1 ≤ n ≤ 105.

[input] integer m

The number of columns.

Guaranteed constraints:
1 ≤ m ≤ 105.

[output] integer

The number of black cells.
"""